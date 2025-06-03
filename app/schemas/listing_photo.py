from pydantic import BaseModel
from typing import Optional
from .base import BaseSchema

class ListingPhotoBase(BaseSchema):
    listing_id: int
    path: str

class ListingPhotoCreate(ListingPhotoBase):
    pass

class ListingPhotoUpdate(BaseModel):
    path: Optional[str] = None

class ListingPhotoResponse(ListingPhotoBase):
    id: int

    class Config:
        orm_mode = True 