from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.core.dependencies import get_db
from app.core.permissions import require_admin
from app.models.user import User
from app.schemas.knowledge_base import (
    ArticleCreate,
    ArticleResponse,
    ArticleUpdate,
)
from app.services.knowledge_base_service import KnowledgeBaseService

router = APIRouter(
    prefix="/knowledge-base",
    tags=["Knowledge Base"],
)


@router.post("", response_model=ArticleResponse)
def create_article(
    data: ArticleCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    return KnowledgeBaseService.create(db, data, admin)


@router.get("", response_model=list[ArticleResponse])
def list_articles(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return KnowledgeBaseService.get_all(db)


@router.get("/search", response_model=list[ArticleResponse])
def search_articles(
    q: str = Query(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return KnowledgeBaseService.search(db, q)


@router.get("/{article_id}", response_model=ArticleResponse)
def get_article(
    article_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    article = KnowledgeBaseService.get(db, article_id)

    if not article:
        raise HTTPException(404, "Article not found")

    return article


@router.put("/{article_id}", response_model=ArticleResponse)
def update_article(
    article_id: UUID,
    data: ArticleUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    article = KnowledgeBaseService.get(db, article_id)

    if not article:
        raise HTTPException(404, "Article not found")

    return KnowledgeBaseService.update(db, article, data)


@router.delete("/{article_id}")
def delete_article(
    article_id: UUID,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    article = KnowledgeBaseService.get(db, article_id)

    if not article:
        raise HTTPException(404, "Article not found")

    KnowledgeBaseService.delete(db, article)

    return {"message": "Article deleted"}