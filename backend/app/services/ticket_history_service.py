from sqlalchemy.orm import Session

from app.models.ticket_history import TicketHistory, TicketAction


class TicketHistoryService:

    @staticmethod
    def create(
        db: Session,
        ticket_id,
        user_id,
        action,
        message,
        old_value=None,
        new_value=None,
    ):
        entry = TicketHistory(
            ticket_id=ticket_id,
            performed_by=user_id,
            action=action,
            message=message,
            old_value=old_value,
            new_value=new_value,
        )

        db.add(entry)
        db.commit()

    @staticmethod
    def get_ticket_history(db: Session, ticket_id):
        return (
            db.query(TicketHistory)
            .filter(TicketHistory.ticket_id == ticket_id)
            .order_by(TicketHistory.created_at.desc())
            .all()
        )