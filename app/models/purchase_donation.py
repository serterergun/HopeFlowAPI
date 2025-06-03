from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class PurchaseDonation(Base):
    __tablename__ = "purchase_donation"

    id = Column(Integer, primary_key=True, index=True)
    purchase_id = Column(Integer, ForeignKey("purchase.id"), nullable=False)
    charity_id = Column(Integer, ForeignKey("charity.id"), nullable=False)
    percentage = Column(Numeric(5, 2), nullable=False)  # 5 digits total, 2 decimal places

    # Relationships
    purchase = relationship("Purchase", back_populates="donations")
    charity = relationship("Charity", back_populates="donations") 