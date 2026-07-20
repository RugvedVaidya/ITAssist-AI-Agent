from uuid import UUID

from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
)


class CategoryService:

    @staticmethod
    def create(
        db: Session,
        data: CategoryCreate,
    ) -> Category:

        category = Category(
            name=data.name,
            description=data.description,
            department_id=data.department_id,
        )

        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    @staticmethod
    def get_all(
        db: Session,
    ) -> list[Category]:

        return (
            db.query(Category)
            .order_by(Category.name.asc())
            .all()
        )

    @staticmethod
    def get(
        db: Session,
        category_id: UUID,
    ) -> Category | None:

        return db.get(
            Category,
            category_id,
        )

    @staticmethod
    def update(
        db: Session,
        category: Category,
        data: CategoryUpdate,
    ) -> Category:

        updates = data.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(category, key, value)

        db.commit()
        db.refresh(category)

        return category

    @staticmethod
    def delete(
        db: Session,
        category: Category,
    ) -> None:

        db.delete(category)
        db.commit()