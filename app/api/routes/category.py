from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.models import Category
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse
from app.api.routes.base import BaseRouter

class CategoryRouter(BaseRouter[Category, CategoryCreate, CategoryUpdate, CategoryResponse]):
    def __init__(self):
        super().__init__(
            model=Category,
            create_schema=CategoryCreate,
            update_schema=CategoryUpdate,
            response_schema=CategoryResponse,
            prefix="/categories",
            tags=["categories"]
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.router.post("/", response_model=CategoryResponse)
        async def create_category(
            category: CategoryCreate,
            db: AsyncSession = Depends(get_db)
        ):
            db_category = Category(**category.model_dump())
            db.add(db_category)
            await db.flush()
            await db.commit()
            await db.refresh(db_category)
            return db_category

        @self.router.get("/", response_model=List[CategoryResponse])
        async def get_categories(
            skip: int = 0,
            limit: int = 100,
            db: AsyncSession = Depends(get_db)
        ):
            result = await db.execute(db.query(Category).offset(skip).limit(limit))
            categories = result.scalars().all()
            return categories

        @self.router.get("/{category_id}", response_model=CategoryResponse)
        async def get_category(
            category_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            category = await db.get(Category, category_id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            return category

        @self.router.put("/{category_id}", response_model=CategoryResponse)
        async def update_category(
            category_id: int,
            category_update: CategoryUpdate,
            db: AsyncSession = Depends(get_db)
        ):
            category = await db.get(Category, category_id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            for field, value in category_update.model_dump(exclude_unset=True).items():
                setattr(category, field, value)
            await db.commit()
            await db.refresh(category)
            return category

        @self.router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_category(
            category_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            category = await db.get(Category, category_id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            await db.delete(category)
            await db.commit()
            return None

router = CategoryRouter().get_router() 