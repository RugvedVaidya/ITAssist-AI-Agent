from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.ticket_history import TicketAction


class TicketHistoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    ticket_id: UUID
    performed_by: UUID
    action: TicketAction
    old_value: str | None
    new_value: str | None
    message: str
    created_at: datetime