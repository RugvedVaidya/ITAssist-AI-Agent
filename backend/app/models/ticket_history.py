import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class TicketAction(str, enum.Enum):
    CREATED = "CREATED"
    UPDATED = "UPDATED"
    ASSIGNED = "ASSIGNED"
    STATUS_CHANGED = "STATUS_CHANGED"
    PRIORITY_CHANGED = "PRIORITY_CHANGED"
    COMMENT_ADDED = "COMMENT_ADDED"
    ATTACHMENT_ADDED = "ATTACHMENT_ADDED"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"


class TicketHistory(Base):
    __tablename__ = "ticket_history"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tickets.id", ondelete="CASCADE"),
        nullable=False,
    )

    performed_by: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    action: Mapped[TicketAction] = mapped_column(
        Enum(TicketAction),
        nullable=False,
    )

    old_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    new_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    message: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    ticket = relationship(
        "Ticket",
        back_populates="history",
    )

    user = relationship(
        "User",
        back_populates="history_entries",
    )