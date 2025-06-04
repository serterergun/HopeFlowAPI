from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.basket import Basket
from app.models.basket_item import BasketItem
from app.models.listing import Listing
from app.schemas.basket import BasketCreate, BasketResponse
from app.schemas.basket_item import BasketItemCreate, BasketItemResponse

router = APIRouter(prefix="/baskets", tags=["baskets"])

@router.post("/", response_model=BasketResponse)
def create_basket(
    basket: BasketCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Create a new basket for the current user."""
    if basket.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create basket for another user"
        )
    
    db_basket = Basket(**basket.model_dump())
    db.add(db_basket)
    db.commit()
    db.refresh(db_basket)
    return db_basket

@router.get("/", response_model=List[BasketResponse])
def get_baskets(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get all baskets for the current user."""
    return db.query(Basket).filter(Basket.user_id == current_user.id).all()

@router.get("/{basket_id}", response_model=BasketResponse)
def get_basket(
    basket_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get a specific basket by ID."""
    basket = db.query(Basket).filter(Basket.id == basket_id).first()
    if not basket:
        raise HTTPException(status_code=404, detail="Basket not found")
    if basket.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this basket")
    return basket

@router.post("/{basket_id}/items", response_model=BasketItemResponse)
def add_item_to_basket(
    basket_id: int,
    item: BasketItemCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Add an item to a basket."""
    # Check basket ownership
    basket = db.query(Basket).filter(Basket.id == basket_id).first()
    if not basket:
        raise HTTPException(status_code=404, detail="Basket not found")
    if basket.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this basket")

    # Check listing availability
    listing = db.query(Listing).filter(Listing.id == item.listing_id).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    if not listing.is_available:
        raise HTTPException(status_code=400, detail="Listing is not available")

    # Create basket item
    db_item = BasketItem(**item.model_dump())
    listing.is_available = False
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{basket_id}/items/{item_id}")
def remove_item_from_basket(
    basket_id: int,
    item_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Remove an item from a basket."""
    # Check basket ownership
    basket = db.query(Basket).filter(Basket.id == basket_id).first()
    if not basket:
        raise HTTPException(status_code=404, detail="Basket not found")
    if basket.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this basket")

    # Find and remove item
    item = db.query(BasketItem).filter(
        BasketItem.id == item_id,
        BasketItem.basket_id == basket_id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in basket")

    # Make listing available again
    item.listing.is_available = True
    db.delete(item)
    db.commit()
    return {"message": "Item removed from basket"} 