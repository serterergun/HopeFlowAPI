from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .base import BaseSchema, TimestampSchema

class UserBase(BaseSchema):
    email: str
    first_name: str
    last_name: str
    phone: Optional[str] = None

class UserCreate(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True 

