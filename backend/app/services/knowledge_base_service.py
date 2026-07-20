from uuid import UUID

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.knowledge_base import KnowledgeBase
from app.models.user import User
from app.schemas.knowledge_base import (
    ArticleCreate,
    ArticleUpdate,
)


class KnowledgeBaseService:

    @staticmethod
    def create(
        db: Session,
        data: ArticleCreate,
        user: User,
    ):

        article = KnowledgeBase(
            title=data.title,
            content=data.content,
            category_id=data.category_id,
            created_by_id=user.id,
        )

        db.add(article)
        db.commit()
        db.refresh(article)

        return article

    @staticmethod
    def get(db: Session, article_id: UUID):
        return db.get(KnowledgeBase, article_id)

    @staticmethod
    def get_all(db: Session):
        return (
            db.query(KnowledgeBase)
            .order_by(KnowledgeBase.created_at.desc())
            .all()
        )

    @staticmethod
    def search(db: Session, query: str):
        return (
            db.query(KnowledgeBase)
            .filter(
                or_(
                    KnowledgeBase.title.ilike(f"%{query}%"),
                    KnowledgeBase.content.ilike(f"%{query}%"),
                )
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        article: KnowledgeBase,
        data: ArticleUpdate,
    ):
        updates = data.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(article, key, value)

        db.commit()
        db.refresh(article)

        return article

    @staticmethod
    def delete(
        db: Session,
        article: KnowledgeBase,
    ):
        db.delete(article)
        db.commit()