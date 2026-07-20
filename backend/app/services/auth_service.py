from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class AuthService:

    @staticmethod
    def create_user(
        db: Session,
        user: UserCreate,
    ) -> User:

        existing = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing:
            raise ValueError("Email already exists")

        db_user = User(
            name=user.name,
            email=user.email,
            password_hash=hash_password(user.password),
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def authenticate_user(
        db: Session,
        email: str,
        password: str,
    ) -> User | None:

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        return user

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str,
    ) -> dict:

        user = AuthService.authenticate_user(
            db,
            email,
            password,
        )

        if not user:
            raise ValueError(
                "Invalid email or password"
            )

        access_token = create_access_token(
            subject=str(user.id)
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }