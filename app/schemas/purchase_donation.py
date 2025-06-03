from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from .base import BaseSchema

class PurchaseDonationBase(BaseSchema):
    purchase_id: int
    charity_id: int
    percentage: Decimal

class PurchaseDonationCreate(PurchaseDonationBase):
    pass

class PurchaseDonationUpdate(BaseModel):
    percentage: Optional[Decimal] = None

class PurchaseDonationResponse(PurchaseDonationBase):
    id: int

    class Config:
        from_attributes = True 