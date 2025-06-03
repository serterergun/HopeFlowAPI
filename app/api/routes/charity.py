from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.models import Charity
from app.schemas import CharityCreate, CharityUpdate, CharityResponse
from app.api.routes.base import BaseRouter

class CharityRouter(BaseRouter[Charity, CharityCreate, CharityUpdate, CharityResponse]):
    def __init__(self):
        super().__init__(
            model=Charity,
            create_schema=CharityCreate,
            update_schema=CharityUpdate,
            response_schema=CharityResponse,
            prefix="/charities",
            tags=["charities"]
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.router.post("/", response_model=CharityResponse)
        async def create_charity(
            charity: CharityCreate,
            db: AsyncSession = Depends(get_db)
        ):
            db_charity = Charity(**charity.model_dump())
            db.add(db_charity)
            await db.flush()
            await db.commit()
            await db.refresh(db_charity)
            return db_charity

        @self.router.get("/", response_model=List[CharityResponse])
        async def get_charities(
            skip: int = 0,
            limit: int = 100,
            db: AsyncSession = Depends(get_db)
        ):
            result = await db.execute(db.query(Charity).offset(skip).limit(limit))
            charities = result.scalars().all()
            return charities

        @self.router.get("/{charity_id}", response_model=CharityResponse)
        async def get_charity(
            charity_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            charity = await db.get(Charity, charity_id)
            if not charity:
                raise HTTPException(status_code=404, detail="Charity not found")
            return charity

        @self.router.put("/{charity_id}", response_model=CharityResponse)
        async def update_charity(
            charity_id: int,
            charity_update: CharityUpdate,
            db: AsyncSession = Depends(get_db)
        ):
            charity = await db.get(Charity, charity_id)
            if not charity:
                raise HTTPException(status_code=404, detail="Charity not found")
            for field, value in charity_update.model_dump(exclude_unset=True).items():
                setattr(charity, field, value)
            await db.commit()
            await db.refresh(charity)
            return charity

        @self.router.delete("/{charity_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_charity(
            charity_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            charity = await db.get(Charity, charity_id)
            if not charity:
                raise HTTPException(status_code=404, detail="Charity not found")
            await db.delete(charity)
            await db.commit()
            return None

router = CharityRouter().get_router() 