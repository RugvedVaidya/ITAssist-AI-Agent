from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CommentCreate(BaseModel):
    content: str
    is_internal: bool = False


class CommentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    content: str
    is_internal: bool

    ticket_id: UUID
    author_id: UUID

    created_at: datetime