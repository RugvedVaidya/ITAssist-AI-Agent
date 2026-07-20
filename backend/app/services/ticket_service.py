from uuid import UUID

from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.models.user import User
from app.schemas.ticket import TicketCreate, TicketUpdate


class TicketService:

    @staticmethod
    def create_ticket(
        db: Session,
        current_user: User,
        data: TicketCreate,
    ) -> Ticket:

        ticket = Ticket(
            title=data.title,
            description=data.description,
            priority=data.priority,
            created_by_id=current_user.id,
        )

        db.add(ticket)
        db.commit()
        db.refresh(ticket)

        return ticket

    @staticmethod
    def get_all_tickets(
        db: Session,
    ):

        return (
            db.query(Ticket)
            .order_by(Ticket.created_at.desc())
            .all()
        )

    @staticmethod
    def get_ticket(
        db: Session,
        ticket_id: UUID,
    ):

        return db.get(
            Ticket,
            ticket_id,
        )

    @staticmethod
    def update_ticket(
        db: Session,
        ticket: Ticket,
        data: TicketUpdate,
    ):

        updates = data.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(ticket, key, value)

        db.commit()
        db.refresh(ticket)

        return ticket

    @staticmethod
    def delete_ticket(
        db: Session,
        ticket: Ticket,
    ):

        db.delete(ticket)
        db.commit()