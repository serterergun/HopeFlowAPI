from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import TypeVar, Generic, Type, Optional, List
from pydantic import BaseModel
from app.core.database import get_db
from app.core.auth import get_current_user

T = TypeVar('T')
CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)
ResponseSchema = TypeVar('ResponseSchema', bound=BaseModel)

class BaseRouter(Generic[T, CreateSchema, UpdateSchema, ResponseSchema]):
    def __init__(
        self,
        model: Type[T],
        create_schema: Type[CreateSchema],
        update_schema: Type[UpdateSchema],
        response_schema: Type[ResponseSchema],
        prefix: str,
        tags: List[str]
    ):
        self.model = model
        self.create_schema = create_schema
        self.update_schema = update_schema
        self.response_schema = response_schema
        self.router = APIRouter(prefix=prefix, tags=tags)

    def get_router(self) -> APIRouter:
        return self.router 