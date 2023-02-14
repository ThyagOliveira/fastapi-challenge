from typing import List

from .. import schemas, models, crud
from ..database import get_db

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter

router = APIRouter()


@router.get("/locations", response_model=List[schemas.Location])
def get_locations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_locations(db=db, skip=skip, limit=limit)


@router.get("/locations/{device_id}", response_model=List[schemas.Location])
def get_locations_by_device(device_id: int, skip: int = 0, limit: int = 10, db:Session = Depends(get_db)):
    if crud.get_device_by_id(db=db, device_id=device_id):
        return crud.get_locations_by_device(db=db, device_id=device_id, skip=skip, limit=limit)

    raise HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Device with id: {device_id} does not exists"
    )


@router.post("/locations", status_code=status.HTTP_201_CREATED, response_model=schemas.Location)
def create_locations(locations: schemas.LocationCreate, db: Session = Depends(get_db)):
    if crud.get_device_by_id(db = db, device_id = locations.device_id):
        return crud.create_locations(db=db, locations=locations)
        
    raise HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Device with id: {locations.device_id} does not exists"
    )
