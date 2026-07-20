from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router
from app.api.ticket import router as ticket_router
from app.api.comment import router as comment_router
from app.api.ticket_history import router as ticket_history_router
from app.api.department import router as department_router
from app.api.category import router as category_router
from app.api.assignment import router as assignment_router
from app.api.attachment import router as attachment_router
from app.api.knowledge_base import router as kb_router
from app.api.ai import router as ai_router
from app.api.rag import router as rag_router

app = FastAPI(
    title="ITAssist AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(ticket_router)
app.include_router(comment_router)
app.include_router(ticket_history_router)
app.include_router(department_router)
app.include_router(category_router)
app.include_router(assignment_router)
app.include_router(attachment_router)
app.include_router(kb_router)
app.include_router(ai_router)
app.include_router(rag_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to ITAssist AI 🚀"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }