from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.core.dependencies import get_db
from app.models.user import User
from app.schemas.ticket_history import TicketHistoryResponse
from app.services.ticket_history_service import TicketHistoryService

router = APIRouter(
    prefix="/tickets/{ticket_id}/history",
    tags=["Ticket History"],
)


@router.get(
    "",
    response_model=list[TicketHistoryResponse],
)
def get_history(
    ticket_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TicketHistoryService.get_ticket_history(db, ticket_id)