from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    main_category_id = Column(Integer, ForeignKey("category.id"), nullable=True)

    # Relationships
    listings = relationship("Listing", back_populates="category")
    subcategories = relationship("Category", backref="main_category", remote_side=[id]) 