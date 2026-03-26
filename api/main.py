from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .models import Base
from .routers import services, bookings, contact, testimonials


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all tables on startup
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Freshious Cleaning API",
    description=("REST API backend for the Freshious Cleaning website. Handles services, booking requests, contact messages, and testimonials."),
    version="1.0.0",
    contact={
        "name": "Freshious Cleaning",
        "email": "hello@freshiouscleaning.com",
    },
    lifespan=lifespan,
)

# ── CORS ────────────────────────────────────────────────────────────────────
# Allow the Django frontend (port 8000) and any local dev origin.
# Tighten origins in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ──────────────────────────────────────────────────────────────────
API_PREFIX = "/api/v1"

app.include_router(services.router, prefix=API_PREFIX)
app.include_router(bookings.router, prefix=API_PREFIX)
app.include_router(contact.router, prefix=API_PREFIX)
app.include_router(testimonials.router, prefix=API_PREFIX)


# ── Health check ─────────────────────────────────────────────────────────────
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "Freshious Cleaning API"}


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to the Freshious Cleaning API 🧹",
        "docs": "/docs",
        "redoc": "/redoc",
    }
