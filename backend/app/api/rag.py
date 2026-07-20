from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.permissions import require_admin
from app.core.dependencies import get_db

from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)


@router.post("/index")
def build_index(
    db: Session = Depends(get_db),
    admin=Depends(require_admin),
):

    count = RAGService.build_index(db)

    return {
        "indexed_articles": count
    }