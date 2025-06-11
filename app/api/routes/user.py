from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models import User
from app.schemas import UserCreate, UserUpdate, UserResponse
from app.api.routes.base import BaseRouter
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)

class UserRouter(BaseRouter[User, UserCreate, UserUpdate, UserResponse]):
    def __init__(self):
        super().__init__(
            model=User,
            create_schema=UserCreate,
            update_schema=UserUpdate,
            response_schema=UserResponse,
            prefix="/users",
            tags=["users"]
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.router.post("/", response_model=UserResponse)
        async def create_user(
            user: UserCreate,
            db: AsyncSession = Depends(get_db)
        ):
            try:
                # Create user instance with all required fields
                db_user = User(
                    email=user.email,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    phone=user.phone if hasattr(user, 'phone') else None,
                    created_at=datetime.now(timezone.utc)
                )
                db_user.set_password(user.password)

                # Add to database and commit
                db.add(db_user)
                await db.flush()  # Flush to get the ID

                if db_user.id is None:
                    raise Exception("Failed to generate user ID")

                await db.commit()
                await db.refresh(db_user)

                logger.info(f"Created user with ID: {db_user.id}")
                return db_user

            except Exception as e:
                await db.rollback()
                logger.error(f"Error creating user: {str(e)}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Failed to create user: {str(e)}"
                )

        @self.router.get("/me", response_model=UserResponse)
        async def read_users_me(current_user: User = Depends(get_current_user)):

            return current_user

        @self.router.get("/", response_model=List[UserResponse])
        async def get_users(
            skip: int = 0,
            limit: int = 100,
            db: AsyncSession = Depends(get_db),
            current_user: User = Depends(get_current_user)
        ):
            users = await db.execute(
                db.query(User).offset(skip).limit(limit)
            )
            users = users.scalars().all()
            return users

        @self.router.get("/{user_id}", response_model=UserResponse)
        async def get_user(
            user_id: int,
            db: AsyncSession = Depends(get_db),
            current_user: User = Depends(get_current_user)
        ):
            user = await db.get(User, user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user

        @self.router.put("/{user_id}", response_model=UserResponse)
        async def update_user(
            user_id: int,
            user_update: UserUpdate,
            db: AsyncSession = Depends(get_db),
            current_user: User = Depends(get_current_user)
        ):
            user = await db.get(User, user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            
            for field, value in user_update.model_dump(exclude_unset=True).items():
                setattr(user, field, value)
            
            await db.commit()
            await db.refresh(user)
            return user

        @self.router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_user(
            user_id: int,
            db: AsyncSession = Depends(get_db),
            current_user: User = Depends(get_current_user)
        ):
            user = await db.get(User, user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            
            await db.delete(user)
            await db.commit()
            return None

        

router = UserRouter().get_router() 