from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.models import Purchase
from app.schemas import PurchaseCreate, PurchaseUpdate, PurchaseResponse
from app.api.routes.base import BaseRouter

class PurchaseRouter(BaseRouter[Purchase, PurchaseCreate, PurchaseUpdate, PurchaseResponse]):
    def __init__(self):
        super().__init__(
            model=Purchase,
            create_schema=PurchaseCreate,
            update_schema=PurchaseUpdate,
            response_schema=PurchaseResponse,
            prefix="/purchases",
            tags=["purchases"]
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.router.post("/", response_model=PurchaseResponse)
        async def create_purchase(
            purchase: PurchaseCreate,
            db: AsyncSession = Depends(get_db)
        ):
            db_purchase = Purchase(**purchase.model_dump())
            db.add(db_purchase)
            await db.flush()
            await db.commit()
            await db.refresh(db_purchase)
            return db_purchase

        @self.router.get("/", response_model=List[PurchaseResponse])
        async def get_purchases(
            skip: int = 0,
            limit: int = 100,
            db: AsyncSession = Depends(get_db)
        ):
            result = await db.execute(db.query(Purchase).offset(skip).limit(limit))
            purchases = result.scalars().all()
            return purchases

        @self.router.get("/{purchase_id}", response_model=PurchaseResponse)
        async def get_purchase(
            purchase_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            purchase = await db.get(Purchase, purchase_id)
            if not purchase:
                raise HTTPException(status_code=404, detail="Purchase not found")
            return purchase

        @self.router.put("/{purchase_id}", response_model=PurchaseResponse)
        async def update_purchase(
            purchase_id: int,
            purchase_update: PurchaseUpdate,
            db: AsyncSession = Depends(get_db)
        ):
            purchase = await db.get(Purchase, purchase_id)
            if not purchase:
                raise HTTPException(status_code=404, detail="Purchase not found")
            for field, value in purchase_update.model_dump(exclude_unset=True).items():
                setattr(purchase, field, value)
            await db.commit()
            await db.refresh(purchase)
            return purchase

        @self.router.delete("/{purchase_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_purchase(
            purchase_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            purchase = await db.get(Purchase, purchase_id)
            if not purchase:
                raise HTTPException(status_code=404, detail="Purchase not found")
            await db.delete(purchase)
            await db.commit()
            return None

router = PurchaseRouter().get_router() 