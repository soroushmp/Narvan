# Make FastAPI Instance and Settings (Like Middlewares and Events)
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routers import contacts

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(contacts.router, tags=['contacts'])
