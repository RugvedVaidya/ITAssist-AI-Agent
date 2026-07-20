from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.permissions import require_admin

from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse,
)

from app.services.department_service import DepartmentService

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)


@router.post("", response_model=DepartmentResponse)
def create_department(
    data: DepartmentCreate,
    db: Session = Depends(get_db),
    admin=Depends(require_admin),
):
    return DepartmentService.create(db, data)


@router.get("", response_model=list[DepartmentResponse])
def get_departments(
    db: Session = Depends(get_db),
):
    return DepartmentService.get_all(db)


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(
    department_id: UUID,
    db: Session = Depends(get_db),
):

    department = DepartmentService.get(db, department_id)

    if not department:
        raise HTTPException(404, "Department not found")

    return department


@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department(
    department_id: UUID,
    data: DepartmentUpdate,
    db: Session = Depends(get_db),
    admin=Depends(require_admin),
):

    department = DepartmentService.get(db, department_id)

    if not department:
        raise HTTPException(404, "Department not found")

    return DepartmentService.update(db, department, data)


@router.delete("/{department_id}")
def delete_department(
    department_id: UUID,
    db: Session = Depends(get_db),
    admin=Depends(require_admin),
):

    department = DepartmentService.get(db, department_id)

    if not department:
        raise HTTPException(404, "Department not found")

    DepartmentService.delete(db, department)

    return {"message": "Department deleted"}