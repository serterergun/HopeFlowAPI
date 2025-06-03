from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from decimal import Decimal

class BaseSchema(BaseModel):
    """Base schema with common configuration"""
    model_config = ConfigDict(from_attributes=True)

class TimestampSchema(BaseSchema):
    """Base schema with timestamp fields"""
    created_at: datetime
    # updated_at: Optional[datetime] = None 