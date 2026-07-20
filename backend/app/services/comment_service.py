from uuid import UUID

from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.models.user import User
from app.schemas.comment import CommentCreate


class CommentService:

    @staticmethod
    def create_comment(
        db: Session,
        ticket_id: UUID,
        current_user: User,
        data: CommentCreate,
    ):

        comment = Comment(
            content=data.content,
            is_internal=data.is_internal,
            ticket_id=ticket_id,
            author_id=current_user.id,
        )

        db.add(comment)
        db.commit()
        db.refresh(comment)

        return comment

    @staticmethod
    def get_comments(
        db: Session,
        ticket_id: UUID,
    ):

        return (
            db.query(Comment)
            .filter(Comment.ticket_id == ticket_id)
            .order_by(Comment.created_at)
            .all()
        )