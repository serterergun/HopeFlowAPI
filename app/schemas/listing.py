from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime
from .base import BaseSchema, TimestampSchema

class UserInfo(BaseModel):
    first_name: str
    last_name_initial: str

    class Config:
        orm_mode = True

class ListingBase(BaseSchema):
    title: str
    description: Optional[str] = None
    category_id: int
    original_price: Optional[Decimal] = None
    usage_duration: Optional[int] = None
    suggested_price: Optional[Decimal] = None
    given_price: Optional[Decimal] = None
    post_code: Optional[str] = None
    user_id: Optional[int] = None

class ListingCreate(BaseModel):
    title: str
    description: Optional[str] = None
    category_id: int
    original_price: Optional[Decimal] = None
    usage_duration: Optional[int] = None
    suggested_price: Optional[Decimal] = None
    given_price: Optional[Decimal] = None
    post_code: Optional[str] = None
    user_id: int

class ListingUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    original_price: Optional[Decimal] = None
    usage_duration: Optional[int] = None
    suggested_price: Optional[Decimal] = None
    given_price: Optional[Decimal] = None
    post_code: Optional[str] = None
    user_id: Optional[int] = None

class ListingResponse(ListingBase, TimestampSchema):
    id: int
    created_at: datetime
    user_info: Optional[UserInfo] = None

    class Config:
        orm_mode = True 