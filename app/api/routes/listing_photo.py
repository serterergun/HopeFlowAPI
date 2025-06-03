from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.models import ListingPhoto
from app.schemas import ListingPhotoCreate, ListingPhotoUpdate, ListingPhotoResponse
from app.api.routes.base import BaseRouter

class ListingPhotoRouter(BaseRouter[ListingPhoto, ListingPhotoCreate, ListingPhotoUpdate, ListingPhotoResponse]):
    def __init__(self):
        super().__init__(
            model=ListingPhoto,
            create_schema=ListingPhotoCreate,
            update_schema=ListingPhotoUpdate,
            response_schema=ListingPhotoResponse,
            prefix="/listing-photos",
            tags=["listing-photos"]
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.router.post("/", response_model=ListingPhotoResponse)
        async def create_listing_photo(
            photo: ListingPhotoCreate,
            db: AsyncSession = Depends(get_db)
        ):
            db_photo = ListingPhoto(**photo.model_dump())
            db.add(db_photo)
            await db.flush()
            await db.commit()
            await db.refresh(db_photo)
            return db_photo

        @self.router.get("/", response_model=List[ListingPhotoResponse])
        async def get_listing_photos(
            skip: int = 0,
            limit: int = 100,
            db: AsyncSession = Depends(get_db)
        ):
            result = await db.execute(db.query(ListingPhoto).offset(skip).limit(limit))
            photos = result.scalars().all()
            return photos

        @self.router.get("/{photo_id}", response_model=ListingPhotoResponse)
        async def get_listing_photo(
            photo_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            photo = await db.get(ListingPhoto, photo_id)
            if not photo:
                raise HTTPException(status_code=404, detail="ListingPhoto not found")
            return photo

        @self.router.put("/{photo_id}", response_model=ListingPhotoResponse)
        async def update_listing_photo(
            photo_id: int,
            photo_update: ListingPhotoUpdate,
            db: AsyncSession = Depends(get_db)
        ):
            photo = await db.get(ListingPhoto, photo_id)
            if not photo:
                raise HTTPException(status_code=404, detail="ListingPhoto not found")
            for field, value in photo_update.model_dump(exclude_unset=True).items():
                setattr(photo, field, value)
            await db.commit()
            await db.refresh(photo)
            return photo

        @self.router.delete("/{photo_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_listing_photo(
            photo_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            photo = await db.get(ListingPhoto, photo_id)
            if not photo:
                raise HTTPException(status_code=404, detail="ListingPhoto not found")
            await db.delete(photo)
            await db.commit()
            return None

router = ListingPhotoRouter().get_router() 