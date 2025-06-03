from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.models import ListingMessage
from app.schemas import ListingMessageCreate, ListingMessageUpdate, ListingMessageResponse
from app.api.routes.base import BaseRouter

class ListingMessageRouter(BaseRouter[ListingMessage, ListingMessageCreate, ListingMessageUpdate, ListingMessageResponse]):
    def __init__(self):
        super().__init__(
            model=ListingMessage,
            create_schema=ListingMessageCreate,
            update_schema=ListingMessageUpdate,
            response_schema=ListingMessageResponse,
            prefix="/listing-messages",
            tags=["listing-messages"]
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.router.post("/", response_model=ListingMessageResponse)
        async def create_listing_message(
            message: ListingMessageCreate,
            db: AsyncSession = Depends(get_db)
        ):
            db_message = ListingMessage(**message.model_dump())
            db.add(db_message)
            await db.flush()
            await db.commit()
            await db.refresh(db_message)
            return db_message

        @self.router.get("/", response_model=List[ListingMessageResponse])
        async def get_listing_messages(
            skip: int = 0,
            limit: int = 100,
            db: AsyncSession = Depends(get_db)
        ):
            result = await db.execute(db.query(ListingMessage).offset(skip).limit(limit))
            messages = result.scalars().all()
            return messages

        @self.router.get("/{message_id}", response_model=ListingMessageResponse)
        async def get_listing_message(
            message_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            message = await db.get(ListingMessage, message_id)
            if not message:
                raise HTTPException(status_code=404, detail="ListingMessage not found")
            return message

        @self.router.put("/{message_id}", response_model=ListingMessageResponse)
        async def update_listing_message(
            message_id: int,
            message_update: ListingMessageUpdate,
            db: AsyncSession = Depends(get_db)
        ):
            message = await db.get(ListingMessage, message_id)
            if not message:
                raise HTTPException(status_code=404, detail="ListingMessage not found")
            for field, value in message_update.model_dump(exclude_unset=True).items():
                setattr(message, field, value)
            await db.commit()
            await db.refresh(message)
            return message

        @self.router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_listing_message(
            message_id: int,
            db: AsyncSession = Depends(get_db)
        ):
            message = await db.get(ListingMessage, message_id)
            if not message:
                raise HTTPException(status_code=404, detail="ListingMessage not found")
            await db.delete(message)
            await db.commit()
            return None

router = ListingMessageRouter().get_router() 