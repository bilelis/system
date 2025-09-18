from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_active_user
from app.core.permissions import check_permissions
from app.models.user import User, UserRole
from app.models.room import Room, RoomStatus
from app.schemas.room import RoomCreate, RoomUpdate, RoomResponse

router = APIRouter()

@router.get("/", response_model=List[RoomResponse])
@check_permissions([UserRole.admin, UserRole.receptionist])
async def list_rooms(
    status: RoomStatus = None,
    floor: int = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    query = db.query(Room)
    if status:
        query = query.filter(Room.status == status)
    if floor:
        query = query.filter(Room.floor == floor)
    
    return query.all()

@router.post("/", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
@check_permissions([UserRole.admin])
async def create_room(
    room: RoomCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Check if room number exists
    db_room = db.query(Room).filter(Room.room_number == room.room_number).first()
    if db_room:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Room number already exists"
        )
    
    new_room = Room(**room.dict())
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

@router.get("/{room_id}", response_model=RoomResponse)
@check_permissions([UserRole.admin, UserRole.receptionist])
async def get_room(
    room_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found"
        )
    return room

@router.patch("/{room_id}", response_model=RoomResponse)
@check_permissions([UserRole.admin, UserRole.receptionist])
async def update_room(
    room_id: str,
    room_update: RoomUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found"
        )
    
    # Update room with non-null values
    for field, value in room_update.dict(exclude_unset=True).items():
        setattr(room, field, value)
    
    db.commit()
    db.refresh(room)
    return room

@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT)
@check_permissions([UserRole.admin])
async def delete_room(
    room_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found"
        )
    
    db.delete(room)
    db.commit()
    return None