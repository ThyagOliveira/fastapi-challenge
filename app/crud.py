from sqlalchemy.orm import Session

from . import models, schemas


def get_device_by_id(db: Session, device_id: int):
    return db.query(models.Device).filter(models.Device.id == device_id).first()


def get_devices(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Device).offset(skip).limit(limit).all()


def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)

    return db_device


def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Location).offset(skip).limit(limit).all()


def get_locations_by_device(db: Session, device_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Location).filter(models.Location.device_id == device_id).offset(skip).limit(limit).all()


def create_locations(db: Session, locations: schemas.LocationCreate):
    db_locations = models.Location(**locations.dict())
    db.add(db_locations)
    db.commit()
    db.refresh(db_locations)

    return db_locations