from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import routes.tickets as tickets
from config import ALLOWED_ORIGINS
from db import init_db
from errors import InvalidProjectName, TicketNotFound


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # creates the tickets table if it doesn't exist yet; skips it if it does
    yield


app = FastAPI(title="Mt. SAC CS Bug Board", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Content-Type"],
)

app.include_router(tickets.router)


# turns domain errors into http responses
@app.exception_handler(TicketNotFound)
def ticket_not_found_handler(request: Request, exc: TicketNotFound):
    return JSONResponse(status_code=404, content={"detail": "Ticket not found"})


@app.exception_handler(InvalidProjectName)
def invalid_project_handler(request: Request, exc: InvalidProjectName):
    return JSONResponse(status_code=422, content={"detail": "Project name is empty after cleaning"})


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def status():
    return {"status": "ok"}