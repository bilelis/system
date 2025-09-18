from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models import outlet, item, order, order_line, guest
from app.core.security import create_access_token
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Models for login
class OutletLoginRequest(BaseModel):
    code: str

class OutletLoginResponse(BaseModel):
    access_token: str
    outlet_id: str
    outlet_name: str
    token_type: str = "bearer"

@router.post("/login", response_model=OutletLoginResponse)
def login_outlet(data: OutletLoginRequest, db: Session = Depends(get_db)):
    outlet_obj = db.query(outlet.Outlet).filter(outlet.Outlet.code == data.code).first()
    if not outlet_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid outlet code")
    token = create_access_token({"outlet_id": str(outlet_obj.id), "outlet_name": outlet_obj.name})
    return OutletLoginResponse(access_token=token, outlet_id=str(outlet_obj.id), outlet_name=outlet_obj.name)

# Items CRUD
@router.get("/items", response_model=List[item.ItemResponse])
def get_items(outlet_id: str, db: Session = Depends(get_db)):
    return db.query(item.Item).filter(item.Item.outlet_id == outlet_id).all()

@router.post("/items", response_model=item.ItemResponse)
def add_item(data: item.ItemCreate, db: Session = Depends(get_db)):
    new_item = item.Item(**data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Orders CRUD
@router.get("/orders", response_model=List[order.OrderResponse])
def get_orders(outlet_id: str, db: Session = Depends(get_db)):
    return db.query(order.Order).filter(order.Order.outlet_id == outlet_id).all()

@router.post("/orders", response_model=order.OrderResponse)
def add_order(data: order.OrderCreate, db: Session = Depends(get_db)):
    new_order = order.Order(**data.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

# PDF Export & Analytics endpoints would be added here