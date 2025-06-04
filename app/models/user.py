from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime, timezone
from app.core.auth import get_password_hash
from typing import Optional

class User(Base):
    """User model"""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    
    # Relationships
    purchases = relationship("Purchase", back_populates="user", cascade="all, delete-orphan")
    
    # ListingMessage relationships
    listing_messages = relationship("ListingMessage", back_populates="user", cascade="all, delete-orphan")
    baskets = relationship("Basket", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password: str):
        """Hash and set the user's password"""
        self.hashed_password = get_password_hash(password) 