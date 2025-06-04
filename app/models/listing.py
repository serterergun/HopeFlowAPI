from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, Text, Enum, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import enum
from app.core.database import Base

class Listing(Base):
    __tablename__ = "listing"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    original_price = Column(Numeric(10, 2), nullable=True)
    usage_duration = Column(Integer, nullable=True)  # in months or days, as needed
    suggested_price = Column(Numeric(10, 2), nullable=True)
    given_price = Column(Numeric(10, 2), nullable=True)
    post_code = Column(String(20), nullable=True)
    is_available = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    category = relationship("Category", back_populates="listings")
    photos = relationship("ListingPhoto", back_populates="listing", cascade="all, delete-orphan")
    messages = relationship("ListingMessage", back_populates="listing", cascade="all, delete-orphan")
    basket_items = relationship("BasketItem", back_populates="listing", cascade="all, delete-orphan") 