from pydantic import BaseModel
from typing import Optional
from .base import BaseSchema

class CategoryBase(BaseSchema):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True 