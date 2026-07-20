import enum
import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Enum, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.db.database import Base


class UserRole(str, enum.Enum):
    USER = "USER"
    SUPPORT = "SUPPORT"
    ADMIN = "ADMIN"


class User(Base):
    __tablename__ = "users"

    # ==========================
    # Primary Key
    # ==========================
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # ==========================
    # Basic Information
    # ==========================
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    avatar_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # ==========================
    # User Role
    # ==========================
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole),
        default=UserRole.USER,
        nullable=False,
    )

    # ==========================
    # Account Status
    # ==========================
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ==========================
    # Audit Fields
    # ==========================
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # ==========================
    # Relationships
    # ==========================
    created_tickets: Mapped[list["Ticket"]] = relationship(
        "Ticket",
        foreign_keys="Ticket.created_by_id",
        back_populates="created_by",
        cascade="all, delete-orphan",
    )

    assigned_tickets: Mapped[list["Ticket"]] = relationship(
        "Ticket",
        foreign_keys="Ticket.assigned_to_id",
        back_populates="assigned_to",
    )
    
    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="author",
    )
    
    history_entries: Mapped[list["TicketHistory"]] = relationship(
        "TicketHistory",
        back_populates="user",
    )
    
    department_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=True,
    )
    
    department: Mapped["Department | None"] = relationship(
        "Department",
        back_populates="users",
    )