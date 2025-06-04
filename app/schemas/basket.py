from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .base import BaseSchema

class BasketBase(BaseSchema):
    user_id: int

class BasketCreate(BasketBase):
    pass

class BasketUpdate(BaseModel):
    pass

class BasketResponse(BasketBase):
    id: int
    created_at: datetime
    items: List["BasketItemResponse"]

    class Config:
        from_attributes = True 