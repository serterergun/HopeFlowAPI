from app.api.routes.base import BaseRouter
from app.models.purchase_donation import PurchaseDonation
from app.schemas.purchase_donation import (
    PurchaseDonationBase,
    PurchaseDonationCreate,
    PurchaseDonationUpdate,
    PurchaseDonationResponse,
)

class PurchaseDonationRouter(BaseRouter):
    def __init__(self):
        super().__init__(
            model=PurchaseDonation,
            create_schema=PurchaseDonationCreate,
            update_schema=PurchaseDonationUpdate,
            response_schema=PurchaseDonationResponse,
            prefix="/purchase-donations",
            tags=["purchase-donations"],
        )

    def _setup_routes(self):
        super()._setup_routes()

router = PurchaseDonationRouter().router 