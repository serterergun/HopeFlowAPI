from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.models import Listing
from app.schemas import ListingCreate, ListingUpdate, ListingResponse
from app.api.routes.base import BaseRouter

class ListingRouter(BaseRouter[Listing, ListingCreate, ListingUpdate, ListingResponse]):
    def __init__(self):
        super().__init__(
            model=Listing,
            create_schema=ListingCreate,
            update_schema=ListingUpdate,
            response_schema=ListingResponse,
            prefix="/listings",
            tags=["listings"]
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.router.post("/", response_model=ListingResponse)
        async def create_listing(
            listing: ListingCreate,
            db: AsyncSession = Depends(get_db)
        ):
            db_listing = Listing(**listing.model_dump())
            db.add(db_listing)
            await db.flush()
            await db.commit()
            await db.refresh(db_listing)
            return db_listing

        @self.router.get("/", response_model=List[ListingResponse])
        async def get_listings(
            skip: int = 0,
            limit: int = 100,
            db: AsyncSession = Depends(get_db)
        ):
            result = await db.execute(db.query(Listing).offset(skip).limit(limit))
            listings = result.scalars().all()
            return listings

        @self.router.get("/{listing_id}", response_model=ListingResponse)
        async def get_listing(
            listing_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            listing = await db.get(Listing, listing_id)
            if not listing:
                raise HTTPException(status_code=404, detail="Listing not found")
            return listing

        @self.router.put("/{listing_id}", response_model=ListingResponse)
        async def update_listing(
            listing_id: int,
            listing_update: ListingUpdate,
            db: AsyncSession = Depends(get_db)
        ):
            listing = await db.get(Listing, listing_id)
            if not listing:
                raise HTTPException(status_code=404, detail="Listing not found")
            for field, value in listing_update.model_dump(exclude_unset=True).items():
                setattr(listing, field, value)
            await db.commit()
            await db.refresh(listing)
            return listing

        @self.router.delete("/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_listing(
            listing_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            listing = await db.get(Listing, listing_id)
            if not listing:
                raise HTTPException(status_code=404, detail="Listing not found")
            await db.delete(listing)
            await db.commit()
            return None

router = ListingRouter().get_router() 