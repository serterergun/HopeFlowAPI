from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .base import BaseSchema

class ListingMessageBase(BaseSchema):
    user_id: int
    listing_id: int
    text: str

class ListingMessageCreate(ListingMessageBase):
    pass

class ListingMessageUpdate(BaseModel):
    text: Optional[str] = None

class ListingMessageResponse(ListingMessageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True 