from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.permissions import require_admin

from app.schemas.rag import (
    SearchRequest,
    SearchResponse,
    Source,
)

from app.services.rag_service import (
    RAGService,
)

from app.ai.rag import (
    RAGEngine,
)

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
        "message": "Knowledge Base indexed successfully.",
        "indexed_articles": count,
    }


@router.post(
    "/search",
    response_model=SearchResponse,
)
def semantic_search(
    request: SearchRequest,
):

    results = RAGService.search(
        request.query,
    )

    sources = []

    for document, score in results:

        sources.append(
            Source(
                title=document.metadata.get(
                    "title",
                    "Unknown",
                ),
                score=float(score),
            )
        )

    return SearchResponse(
        sources=sources,
    )


@router.post("/ask")
def ask_ai(
    request: SearchRequest,
):

    return RAGEngine.ask(
        request.query,
    )