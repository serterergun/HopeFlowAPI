from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime
from .base import BaseSchema, TimestampSchema

class ListingBase(BaseSchema):
    title: str
    description: Optional[str] = None
    category_id: int
    original_price: Optional[Decimal] = None
    usage_duration: Optional[int] = None
    suggested_price: Optional[Decimal] = None
    given_price: Optional[Decimal] = None
    post_code: Optional[str] = None

class ListingCreate(ListingBase):
    pass

class ListingUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    original_price: Optional[Decimal] = None
    usage_duration: Optional[int] = None
    suggested_price: Optional[Decimal] = None
    given_price: Optional[Decimal] = None
    post_code: Optional[str] = None

class ListingResponse(ListingBase, TimestampSchema):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True 