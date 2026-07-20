from uuid import UUID

from sqlalchemy.orm import Session

from app.models.user import User


class UserService:

    @staticmethod
    def get(
        db: Session,
        user_id: UUID,
    ) -> User | None:

        return db.get(
            User,
            user_id,
        )