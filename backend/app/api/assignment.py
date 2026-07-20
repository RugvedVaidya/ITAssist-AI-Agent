from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.permissions import require_admin

from app.models.user import User

from app.services.ticket_service import TicketService
from app.services.assignment_service import AssignmentService

from app.schemas.assignment import TicketAssignment

from app.services.user_service import UserService

router = APIRouter(
    prefix="/assignments",
    tags=["Assignments"],
)


@router.put("/{ticket_id}")
def assign_ticket(
    ticket_id: UUID,
    data: TicketAssignment,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):

    ticket = TicketService.get_ticket(
        db,
        ticket_id,
    )

    if not ticket:
        raise HTTPException(
            404,
            "Ticket not found",
        )

    support = UserService.get(
        db,
        data.support_user_id,
    )

    if not support:
        raise HTTPException(
            404,
            "Support engineer not found",
        )

    try:
        return AssignmentService.assign_ticket(
            db,
            ticket,
            support,
            admin,
        )

    except ValueError as e:
        raise HTTPException(
            400,
            str(e),
        )


@router.delete("/{ticket_id}")
def unassign_ticket(
    ticket_id: UUID,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):

    ticket = TicketService.get_ticket(
        db,
        ticket_id,
    )

    if not ticket:
        raise HTTPException(
            404,
            "Ticket not found",
        )

    return AssignmentService.unassign_ticket(
        db,
        ticket,
        admin,
    )