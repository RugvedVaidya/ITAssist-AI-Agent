from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.attachment import Attachment
from app.models.ticket import Ticket
from app.models.user import User
from app.utils.file_storage import save_upload


class AttachmentService:

    @staticmethod
    def upload(
        db: Session,
        ticket: Ticket,
        user: User,
        file: UploadFile,
    ):

        stored_name, path = save_upload(file)

        attachment = Attachment(
            filename=file.filename,
            stored_filename=stored_name,
            content_type=file.content_type,
            file_size=file.size or 0,
            file_path=path,
            ticket_id=ticket.id,
            uploaded_by_id=user.id,
        )

        db.add(attachment)
        db.commit()
        db.refresh(attachment)

        return attachment

    @staticmethod
    def get_ticket_files(
        db: Session,
        ticket_id,
    ):
        return (
            db.query(Attachment)
            .filter(Attachment.ticket_id == ticket_id)
            .all()
        )