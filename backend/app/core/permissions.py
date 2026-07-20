from fastapi import Depends, HTTPException, status

from app.core.auth import get_current_user
from app.models.user import User, UserRole


def require_admin(
    current_user: User = Depends(get_current_user),
):

    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return current_user


def require_support(
    current_user: User = Depends(get_current_user),
):

    if current_user.role not in (
        UserRole.ADMIN,
        UserRole.SUPPORT,
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Support access required",
        )

    return current_user