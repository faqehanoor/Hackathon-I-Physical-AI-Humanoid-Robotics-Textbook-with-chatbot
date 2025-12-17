import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.api.books import router as books_router
from src.api.ai import router as ai_router
from src.utils.exceptions import add_exception_handlers

# Load environment variables
load_dotenv()

app = FastAPI(
    title="AI-Native Book Backend",
    description="Backend API for AI-powered book processing and management",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers
add_exception_handlers(app)

# Include routers
app.include_router(books_router, prefix="/api/v1", tags=["books"])
app.include_router(ai_router, prefix="/api/v1", tags=["ai"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Native Book Backend"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

def run_dev_server():
    """Run the development server"""
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_dirs=["src"]
    )


def run_prod_server():
    """Run the production server"""
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        workers=4
    )