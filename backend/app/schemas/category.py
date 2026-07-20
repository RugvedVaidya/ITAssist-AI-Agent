from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CategoryCreate(BaseModel):
    name: str
    description: str | None = None
    department_id: UUID


class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    department_id: UUID | None = None


class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str | None
    department_id: UUID
    created_at: datetime