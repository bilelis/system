from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_active_user
from app.core.permissions import check_permissions
from app.models.user import User, UserRole
from app.models.guest import Guest
from app.schemas.guest import GuestCreate, GuestUpdate, GuestResponse

router = APIRouter()

@router.get("/", response_model=List[GuestResponse])
@check_permissions([UserRole.admin, UserRole.receptionist])
async def list_guests(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return db.query(Guest).all()

@router.post("/", response_model=GuestResponse, status_code=status.HTTP_201_CREATED)
@check_permissions([UserRole.admin, UserRole.receptionist])
async def create_guest(guest: GuestCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    new_guest = Guest(**guest.dict())
    db.add(new_guest)
    db.commit()
    db.refresh(new_guest)
    return new_guest

@router.get("/{guest_id}", response_model=GuestResponse)
@check_permissions([UserRole.admin, UserRole.receptionist])
async def get_guest(guest_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    guest = db.query(Guest).filter(Guest.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guest not found")
    return guest

@router.patch("/{guest_id}", response_model=GuestResponse)
@check_permissions([UserRole.admin, UserRole.receptionist])
async def update_guest(guest_id: str, guest_update: GuestUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    guest = db.query(Guest).filter(Guest.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guest not found")
    for field, value in guest_update.dict(exclude_unset=True).items():
        setattr(guest, field, value)
    db.commit()
    db.refresh(guest)
    return guest

@router.delete("/{guest_id}", status_code=status.HTTP_204_NO_CONTENT)
@check_permissions([UserRole.admin])
async def delete_guest(guest_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    guest = db.query(Guest).filter(Guest.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guest not found")
    db.delete(guest)
    db.commit()
    return None
