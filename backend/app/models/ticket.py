import enum
import uuid
from datetime import datetime

from sqlalchemy import (
    Enum,
    ForeignKey,
    String,
    Text,
    DateTime,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.db.database import Base


class TicketPriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class TicketStatus(str, enum.Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"
    REOPENED = "REOPENED"


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    priority: Mapped[TicketPriority] = mapped_column(
        Enum(TicketPriority),
        default=TicketPriority.MEDIUM,
    )

    status: Mapped[TicketStatus] = mapped_column(
        Enum(TicketStatus),
        default=TicketStatus.OPEN,
    )

    created_by_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    assigned_to_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    created_by = relationship(
        "User",
        foreign_keys=[created_by_id],
    )

    assigned_to = relationship(
        "User",
        foreign_keys=[assigned_to_id],
    )
    
    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="ticket",
        cascade="all, delete-orphan",
    )
    
    history: Mapped[list["TicketHistory"]] = relationship(
        "TicketHistory",
        back_populates="ticket",
        cascade="all, delete-orphan",
    )
    
    category_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id"),
        nullable=True,
    )

    category: Mapped["Category | None"] = relationship(
        "Category",
        back_populates="tickets",
    )
    
    department: Mapped["Department | None"] = relationship(
        "Department",
        back_populates="tickets",
    )
    
    