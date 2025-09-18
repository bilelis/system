from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.room import Room
from app.schemas.room import RoomCreate, RoomUpdate, RoomResponse
from app.api.deps import get_current_active_user

router = APIRouter()

@router.post("/", response_model=RoomResponse)
def create_room(
    room: RoomCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    db_room = Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@router.get("/", response_model=List[RoomResponse])
def read_rooms(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    rooms = db.query(Room).offset(skip).limit(limit).all()
    return rooms

@router.get("/{room_id}", response_model=RoomResponse)
def read_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.put("/{room_id}", response_model=RoomResponse)
def update_room(
    room_id: int,
    room: RoomUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    for key, value in room.dict(exclude_unset=True).items():
        setattr(db_room, key, value)
    
    db.commit()
    db.refresh(db_room)
    return db_room

@router.delete("/{room_id}")
def delete_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    db.delete(db_room)
    db.commit()
    return {"message": "Room deleted successfully"}