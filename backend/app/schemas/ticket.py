from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.ticket import TicketPriority, TicketStatus


class TicketCreate(BaseModel):
    title: str
    description: str
    priority: TicketPriority = TicketPriority.MEDIUM


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: TicketPriority | None = None
    status: TicketStatus | None = None
    assigned_to_id: UUID | None = None


class TicketResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: str
    priority: TicketPriority
    status: TicketStatus

    created_by_id: UUID
    assigned_to_id: UUID | None

    created_at: datetime
    updated_at: datetime