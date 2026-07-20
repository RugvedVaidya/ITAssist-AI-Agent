from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.knowledge_base import ArticleStatus


class ArticleCreate(BaseModel):
    title: str
    content: str
    category_id: UUID | None = None


class ArticleUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    status: ArticleStatus | None = None
    category_id: UUID | None = None


class ArticleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    content: str
    status: ArticleStatus
    category_id: UUID | None
    created_by_id: UUID
    created_at: datetime
    updated_at: datetime