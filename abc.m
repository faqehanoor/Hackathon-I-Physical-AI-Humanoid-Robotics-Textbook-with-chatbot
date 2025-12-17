neon_db_url: psql 'postgresql://neondb_owner:npg_RMp3ychWCg2L@ep-aged-cherry-ah8zb0b2-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

Qdrant link: https://066dbcf1-8341-4072-b4ae-c664e0daaa89.europe-west3-0.gcp.cloud.qdrant.io

cluster_id: 066dbcf1-8341-4072-b4ae-c664e0daaa89

Qdrant Api: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.saY5aFVrwAJCEPw_-PmUDk3iQeQb5taUCai8RBHapyI

cohere api key: XTGgxVCmhGnfoxnOHpTkwSksRd4fAgOJbeaFxLxm



Project: AI-Native Book RAG Chatbot (Qwen + Cohere)

Target Audience:
- Readers of the published book
- Students and educators using the book as a learning resource
- Reviewers evaluating AI-native, spec-driven systems

Primary Goal:
Design and implement a Retrieval-Augmented Generation (RAG) chatbot
embedded within a published book that can accurately answer user questions
based strictly on the book’s content or on user-selected text.

---

System Scope:

The system will:
- Ingest book content into a vector database
- Retrieve relevant passages using semantic search
- Rerank results for precision
- Generate grounded answers using a Qwen language model
- Support a “selected-text-only” answering mode

The system will NOT:
- Use OpenAI APIs
- Answer questions using external knowledge
- Hallucinate or infer beyond provided context
- Train on or permanently store user conversations without consent

---

Technology Stack (Fixed):

- Backend Framework: FastAPI
- Language Model: Qwen (via compatible inference endpoint)
- Embeddings & Reranking: Cohere API
- Vector Database: Qdrant Cloud (Free Tier)
- Relational Database: Neon Serverless Postgres
- Architecture Style: Spec-Driven Development (Spec-Kit Plus)

---

Configuration:

neon_db_url: psql 'postgresql://neondb_owner:npg_RMp3ychWCg2L@ep-aged-cherry-ah8zb0b2-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

Qdrant link: https://066dbcf1-8341-4072-b4ae-c664e0daaa89.europe-west3-0.gcp.cloud.qdrant.io

cluster_id: 066dbcf1-8341-4072-b4ae-c664e0daaa89

Qdrant Api: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.saY5aFVrwAJCEPw_-PmUDk3iQeQb5taUCai8RBHapyI

cohere api key: XTGgxVCmhGnfoxnOHpTkwSksRd4fAgOJbeaFxLxm


---

Core Functional Requirements:

1. Book Content Ingestion
   - Chunk size: 500–800 tokens
   - Overlap: 10–20%
   - Metadata per chunk:
     - book_id
     - chapter
     - section
     - page_number

2. Semantic Retrieval
   - Use Cohere embeddings for vectorization
   - Store and search vectors in Qdrant
   - Retrieve top-K (K ≤ 5) chunks per query

3. Reranking
   - Apply Cohere Rerank to retrieved chunks
   - Ensure highest relevance before generation

4. Answer Generation
   - Use Qwen with low temperature (≤ 0.3)
   - System prompt enforces:
     - Grounded answers only
     - Explicit refusal if context is insufficient

5. Selected-Text Mode
   - When user provides selected text:
     - Bypass Qdrant retrieval
     - Use ONLY the selected text as context
     - Disallow all other sources

6. Traceability
   - Every response must be traceable to:
     - Chunk IDs
     - Page numbers
     - Sections (when available)

---

Success Criteria:

- User receives accurate answers grounded in book content
- Zero hallucinated responses during evaluation
- Selected-text mode fully isolates context
- Retrieval + reranking improves answer precision
- Average response time under 3 seconds
- System can be deployed using free-tier infrastructure

---

Constraints:

- No OpenAI services
- Free-tier friendly (Qdrant + Neon)
- API-first design
- Reproducible setup using environment variables
- Secure handling of all secrets

---

Out of Scope:

- General-purpose chatbot functionality
- Internet or web search augmentation
- Ethical or philosophical analysis of AI
- Model fine-tuning
- UI/UX frontend implementation
