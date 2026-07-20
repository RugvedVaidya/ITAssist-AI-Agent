from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.core.dependencies import get_db
from app.core.permissions import require_admin
from app.models.ticket import Ticket
from app.models.user import User, UserRole
from app.schemas.ticket import (
    TicketCreate,
    TicketResponse,
    TicketUpdate,
)
from app.services.ticket_service import TicketService

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)


@router.post(
    "",
    response_model=TicketResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_ticket(
    data: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TicketService.create_ticket(
        db,
        current_user,
        data,
    )


@router.get(
    "",
    response_model=list[TicketResponse],
)
def get_all_tickets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Admin sees everything
    if current_user.role == UserRole.ADMIN:
        return TicketService.get_all_tickets(db)

    # Support sees assigned tickets
    if current_user.role == UserRole.SUPPORT:
        return (
            db.query(Ticket)
            .filter(Ticket.assigned_to_id == current_user.id)
            .all()
        )

    # Normal users see only their own tickets
    return (
        db.query(Ticket)
        .filter(Ticket.created_by_id == current_user.id)
        .all()
    )


@router.get(
    "/{ticket_id}",
    response_model=TicketResponse,
)
def get_ticket(
    ticket_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ticket = TicketService.get_ticket(
        db,
        ticket_id,
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    # USER can only view their own tickets
    if (
        current_user.role == UserRole.USER
        and ticket.created_by_id != current_user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    # SUPPORT can only view assigned tickets
    if (
        current_user.role == UserRole.SUPPORT
        and ticket.assigned_to_id != current_user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    return ticket


@router.put(
    "/{ticket_id}",
    response_model=TicketResponse,
)
def update_ticket(
    ticket_id: UUID,
    data: TicketUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ticket = TicketService.get_ticket(
        db,
        ticket_id,
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    # USER can update only their own tickets
    if (
        current_user.role == UserRole.USER
        and ticket.created_by_id != current_user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    # SUPPORT can update only assigned tickets
    if (
        current_user.role == UserRole.SUPPORT
        and ticket.assigned_to_id != current_user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    return TicketService.update_ticket(
        db,
        ticket,
        data,
    )


@router.delete(
    "/{ticket_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_ticket(
    ticket_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    ticket = TicketService.get_ticket(
        db,
        ticket_id,
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    TicketService.delete_ticket(
        db,
        ticket,
    )