from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .base import BaseSchema

class BasketItemBase(BaseSchema):
    basket_id: int
    listing_id: int

class BasketItemCreate(BasketItemBase):
    pass

class BasketItemUpdate(BaseModel):
    pass

class BasketItemResponse(BasketItemBase):
    id: int
    created_at: datetime
    is_valid: bool

    class Config:
        from_attributes = True 