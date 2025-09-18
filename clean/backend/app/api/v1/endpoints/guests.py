from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.guest import Guest
from app.schemas.guest import GuestCreate, GuestUpdate, GuestResponse
from app.api.deps import get_current_active_user

router = APIRouter()

@router.post("/", response_model=GuestResponse)
def create_guest(
    guest: GuestCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    db_guest = Guest(**guest.dict())
    db.add(db_guest)
    db.commit()
    db.refresh(db_guest)
    return db_guest

@router.get("/", response_model=List[GuestResponse])
def read_guests(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    guests = db.query(Guest).offset(skip).limit(limit).all()
    return guests

@router.get("/{guest_id}", response_model=GuestResponse)
def read_guest(
    guest_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    guest = db.query(Guest).filter(Guest.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest

@router.put("/{guest_id}", response_model=GuestResponse)
def update_guest(
    guest_id: int,
    guest: GuestUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    db_guest = db.query(Guest).filter(Guest.id == guest_id).first()
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    
    for key, value in guest.dict(exclude_unset=True).items():
        setattr(db_guest, key, value)
    
    db.commit()
    db.refresh(db_guest)
    return db_guest

@router.delete("/{guest_id}")
def delete_guest(
    guest_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    db_guest = db.query(Guest).filter(Guest.id == guest_id).first()
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    
    db.delete(db_guest)
    db.commit()
    return {"message": "Guest deleted successfully"}