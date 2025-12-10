import os
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import Qdrant
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- RAG Pipeline Components ---

# Global variable to hold the RAG chain
rag_chain = None

def get_rag_chain():
    """Initializes and returns the RAG chain."""
    global rag_chain
    if rag_chain is None:
        # 1. Load Documents
        loader = DirectoryLoader(
            "../frontend/docs",
            glob="**/*.md",
            loader_cls=UnstructuredMarkdownLoader,
            show_progress=True,
            use_multithreading=True
        )
        documents = loader.load()

        # 2. Split Documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(documents)

        # 3. Create Embeddings
        embeddings = OpenAIEmbeddings()

        # 4. Create Vector Store
        qdrant = Qdrant.from_documents(
            splits,
            embeddings,
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
            collection_name="ai-native-book",
            force_recreate=True, # Set to False after initial ingestion
        )

        # 5. Create Retriever
        retriever = qdrant.as_retriever()

        # 6. Create Prompt Template
        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        """
        prompt = PromptTemplate.from_template(template)

        # 7. Create LLM
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

        # 8. Create RAG Chain
        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
    return rag_chain

class ChatRequest(BaseModel):
    query: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the RAG Chatbot Backend!"}

@app.post("/chat")
async def chat_with_bot(request: ChatRequest, chain: str = Depends(get_rag_chain)):
    """Handles chat requests by invoking the RAG chain."""
    response = chain.invoke(request.query)
    return {"response": response}

# Optional: To pre-load the model on startup
@app.on_event("startup")
async def startup_event():
    get_rag_chain()