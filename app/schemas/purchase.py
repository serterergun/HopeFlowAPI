from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .base import BaseSchema

class PurchaseBase(BaseSchema):
    listing_id: int
    user_id: int

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseUpdate(BaseModel):
    listing_id: Optional[int] = None
    user_id: Optional[int] = None

class PurchaseResponse(PurchaseBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True 