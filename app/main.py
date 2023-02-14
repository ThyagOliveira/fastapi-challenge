from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import device, location

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(device.router, tags=["Device"], prefix="/api")
app.include_router(location.router, tags=["Location"], prefix="/api")
