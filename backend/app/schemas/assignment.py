from uuid import UUID

from pydantic import BaseModel


class TicketAssignment(BaseModel):
    support_user_id: UUID