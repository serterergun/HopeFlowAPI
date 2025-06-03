from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base

class ListingMessage(Base):
    __tablename__ = "listing_message"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    listing_id = Column(Integer, ForeignKey("listing.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    text = Column(Text, nullable=False)

    # Relationships
    user = relationship("User", back_populates="listing_messages")
    listing = relationship("Listing", back_populates="messages") 