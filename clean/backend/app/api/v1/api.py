from fastapi import APIRouter
from app.api.v1.endpoints import auth, rooms, guests, orders

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
api_router.include_router(guests.router, prefix="/guests", tags=["guests"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])