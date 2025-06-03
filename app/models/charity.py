from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Charity(Base):
    __tablename__ = "charity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

    # Relationships
    donations = relationship("PurchaseDonation", back_populates="charity", cascade="all, delete-orphan") 