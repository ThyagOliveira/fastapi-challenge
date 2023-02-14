from typing import Optional

from pydantic import BaseModel


class DeviceBase(BaseModel):
    device_name: Optional[str | None] = None


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: int

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    latitude: str
    longitude: str


class LocationCreate(LocationBase):
    device_id: int


class Location(LocationBase):
    device_id: Optional[int]

    class Config:
        orm_mode = True
