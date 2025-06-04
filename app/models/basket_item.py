from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone, timedelta
from app.core.database import Base

class BasketItem(Base):
    __tablename__ = "basket_item"

    id = Column(Integer, primary_key=True, index=True)
    basket_id = Column(Integer, ForeignKey("basket.id"), nullable=False)
    listing_id = Column(Integer, ForeignKey("listing.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    basket = relationship("Basket", back_populates="items")
    listing = relationship("Listing", back_populates="basket_items")

    def is_valid(self) -> bool:
        """Check if the basket item is still valid (less than 30 minutes old)"""
        return datetime.now(timezone.utc) - self.created_at < timedelta(minutes=30) 