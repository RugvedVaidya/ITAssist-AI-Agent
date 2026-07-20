from uuid import UUID

from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
)


class DepartmentService:

    @staticmethod
    def create(db: Session, data: DepartmentCreate):

        department = Department(**data.model_dump())

        db.add(department)
        db.commit()
        db.refresh(department)

        return department

    @staticmethod
    def get_all(db: Session):
        return db.query(Department).all()

    @staticmethod
    def get(db: Session, department_id: UUID):
        return db.get(Department, department_id)

    @staticmethod
    def update(db: Session, department: Department, data: DepartmentUpdate):

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(department, key, value)

        db.commit()
        db.refresh(department)

        return department

    @staticmethod
    def delete(db: Session, department: Department):
        db.delete(department)
        db.commit()