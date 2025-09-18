from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_active_user
from app.core.permissions import check_permissions
from app.models.user import User, UserRole
from app.models.order import Order, OrderStatus
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse

router = APIRouter()

@router.get("/", response_model=List[OrderResponse])
@check_permissions([UserRole.admin, UserRole.cashier, UserRole.receptionist])
async def list_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return db.query(Order).all()

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
@check_permissions([UserRole.admin, UserRole.cashier])
async def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/{order_id}", response_model=OrderResponse)
@check_permissions([UserRole.admin, UserRole.cashier, UserRole.receptionist])
async def get_order(order_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

@router.patch("/{order_id}", response_model=OrderResponse)
@check_permissions([UserRole.admin, UserRole.cashier])
async def update_order(order_id: str, order_update: OrderUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    for field, value in order_update.dict(exclude_unset=True).items():
        setattr(order, field, value)
    db.commit()
    db.refresh(order)
    return order

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
@check_permissions([UserRole.admin])
async def delete_order(order_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    db.delete(order)
    db.commit()
    return None