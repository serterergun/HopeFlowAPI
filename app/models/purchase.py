from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base

class Purchase(Base):
    __tablename__ = "purchase"

    id = Column(Integer, primary_key=True, index=True)
    basket_id = Column(Integer, ForeignKey("basket.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    basket = relationship("Basket", back_populates="purchases")
    user = relationship("User", back_populates="purchases")
    donations = relationship("PurchaseDonation", back_populates="purchase", cascade="all, delete-orphan") 