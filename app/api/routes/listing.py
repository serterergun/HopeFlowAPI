from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.models import Listing, User, Category
from app.schemas import ListingCreate, ListingUpdate, ListingResponse
from app.api.routes.base import BaseRouter
from sqlalchemy import select, func

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
            # category_id kontrolü
            category = await db.get(Category, listing.category_id)
            if not category:
                raise HTTPException(status_code=400, detail="Invalid category_id")
            
            # user_id kontrolü
            user = await db.get(User, listing.user_id)
            if not user:
                raise HTTPException(status_code=400, detail="Invalid user_id")
            
            allowed_fields = {c.name for c in Listing.__table__.columns if c.name != "created_at"}
            data = {k: v for k, v in listing.model_dump().items() if k in allowed_fields}
            db_listing = Listing(**data)
            db.add(db_listing)
            await db.flush()
            await db.commit()
            await db.refresh(db_listing)
            return db_listing

        @self.router.get("/", response_model=List[ListingResponse])
        async def get_listings(
            user_id: int | None = None,
            skip: int = 0,
            limit: int = 100,
            db: AsyncSession = Depends(get_db)
        ):
            query = (
                select(
                    Listing,
                    User.first_name,
                    func.substr(User.last_name, 1, 1).label('last_name_initial')
                )
                .join(User, Listing.user_id == User.id)
                .offset(skip)
                .limit(limit)
            )
            
            if user_id is not None:
                query = query.where(Listing.user_id == user_id)
    
            query = query.offset(skip).limit(limit)
    
            result = await db.execute(query)
            rows = result.all()
            
            listings = []
            for row in rows:
                listing_dict = row[0].__dict__
                listing_dict['user_info'] = {
                    'first_name': row[1],
                    'last_name_initial': row[2]
                }
                listings.append(ListingResponse(**listing_dict))
            
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