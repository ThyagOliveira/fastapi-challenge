from typing import List

from .. import schemas, models, crud
from ..database import get_db

from sqlalchemy.orm import Session
from fastapi import Depends, status, APIRouter

router = APIRouter()


@router.get("/devices", response_model=List[schemas.Device])
def get_devices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    devices = crud.get_devices(db=db, skip=skip, limit=limit)
    
    return devices


@router.post("/devices", status_code=status.HTTP_201_CREATED, response_model=schemas.Device)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    return crud.create_device(db=db, device=device)
