from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.models.user import User, UserRole
from app.models.ticket_history import TicketAction
from app.services.ticket_history_service import TicketHistoryService


class AssignmentService:

    @staticmethod
    def assign_ticket(
        db: Session,
        ticket: Ticket,
        support_user: User,
        admin: User,
    ):

        if support_user.role != UserRole.SUPPORT:
            raise ValueError(
                "User is not a support engineer."
            )

        old_assignee = (
            str(ticket.assigned_to_id)
            if ticket.assigned_to_id
            else None
        )

        ticket.assigned_to_id = support_user.id

        db.commit()
        db.refresh(ticket)

        TicketHistoryService.create(
            db=db,
            ticket_id=ticket.id,
            user_id=admin.id,
            action=TicketAction.ASSIGNED,
            message=f"Assigned to {support_user.name}",
            old_value=old_assignee,
            new_value=str(support_user.id),
        )

        return ticket

    @staticmethod
    def unassign_ticket(
        db: Session,
        ticket: Ticket,
        admin: User,
    ):

        old_assignee = (
            str(ticket.assigned_to_id)
            if ticket.assigned_to_id
            else None
        )

        ticket.assigned_to_id = None

        db.commit()
        db.refresh(ticket)

        TicketHistoryService.create(
            db=db,
            ticket_id=ticket.id,
            user_id=admin.id,
            action=TicketAction.ASSIGNED,
            message="Ticket unassigned",
            old_value=old_assignee,
            new_value=None,
        )

        return ticket