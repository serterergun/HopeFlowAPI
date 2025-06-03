from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .base import BaseSchema, TimestampSchema

class UserBase(BaseSchema):
    email: str
    first_name: str
    last_name: str
    is_active: bool = True
    phone: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase, TimestampSchema):
    id: int
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True 

