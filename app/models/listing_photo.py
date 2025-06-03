from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class ListingPhoto(Base):
    __tablename__ = "listing_photo"

    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer, ForeignKey("listing.id"), nullable=False)
    path = Column(String(512), nullable=False)

    # Relationships
    listing = relationship("Listing", back_populates="photos") 