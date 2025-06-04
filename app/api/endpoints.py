from fastapi import APIRouter
from app.api.routes import (
    user_router,
    listing_router,
    category_router,
    listing_photo_router,
    purchase_router,
    listing_message_router,
    charity_router,
    purchase_donation_router,
    basket_router,
)
from app.core.auth import router as auth_router


api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(listing_router)
api_router.include_router(category_router)
api_router.include_router(listing_photo_router)
api_router.include_router(purchase_router)
api_router.include_router(listing_message_router)
api_router.include_router(charity_router)
api_router.include_router(purchase_donation_router)
api_router.include_router(basket_router)
api_router.include_router(auth_router)

router = api_router