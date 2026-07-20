from uuid import UUID

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.core.dependencies import get_db
from app.models.user import User
from app.schemas.attachment import AttachmentResponse
from app.services.attachment_service import AttachmentService
from app.services.ticket_service import TicketService

router = APIRouter(
    prefix="/attachments",
    tags=["Attachments"],
)


@router.post(
    "/{ticket_id}",
    response_model=AttachmentResponse,
)
def upload_attachment(
    ticket_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    ticket = TicketService.get_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(404, "Ticket not found")

    return AttachmentService.upload(
        db,
        ticket,
        current_user,
        file,
    )


@router.get(
    "/{ticket_id}",
    response_model=list[AttachmentResponse],
)
def list_attachments(
    ticket_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return AttachmentService.get_ticket_files(
        db,
        ticket_id,
    )