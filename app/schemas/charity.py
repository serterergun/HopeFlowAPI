from pydantic import BaseModel
from typing import Optional
from .base import BaseSchema

class CharityBase(BaseSchema):
    name: str

class CharityCreate(CharityBase):
    pass

class CharityUpdate(BaseModel):
    name: Optional[str] = None

class CharityResponse(CharityBase):
    id: int

    class Config:
        orm_mode = True 