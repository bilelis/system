from fastapi import APIRouter
from app.api.v1.endpoints import auth, rooms, guests, orders, analytics
from app.api.v1.endpoints.simple_auth import router as simple_auth_router

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(simple_auth_router, prefix="/simple-auth", tags=["Simple Authentication"])
api_router.include_router(rooms.router, prefix="/rooms", tags=["Rooms"])
api_router.include_router(guests.router, prefix="/guests", tags=["Guests"])
api_router.include_router(orders.router, prefix="/orders", tags=["Orders"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])