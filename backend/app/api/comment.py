from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.core.dependencies import get_db
from app.models.user import User
from app.schemas.comment import (
    CommentCreate,
    CommentResponse,
)
from app.services.comment_service import CommentService

router = APIRouter(
    prefix="/tickets/{ticket_id}/comments",
    tags=["Comments"],
)


@router.post(
    "",
    response_model=CommentResponse,
)
def create_comment(
    ticket_id: UUID,
    data: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return CommentService.create_comment(
        db,
        ticket_id,
        current_user,
        data,
    )


@router.get(
    "",
    response_model=list[CommentResponse],
)
def get_comments(
    ticket_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return CommentService.get_comments(
        db,
        ticket_id,
    )