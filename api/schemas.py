from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator


# ───────────────────────── Services ─────────────────────────


class ServiceBase(BaseModel):
    name: str = Field(..., max_length=120)
    slug: str = Field(..., max_length=120)
    description: str
    icon: str = "bi-sparkles"
    price_label: str = "Contact for pricing"
    is_active: bool = True


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=120)
    description: Optional[str] = None
    icon: Optional[str] = None
    price_label: Optional[str] = None
    is_active: Optional[bool] = None


class ServiceOut(ServiceBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


# ───────────────────────── Bookings ─────────────────────────


class BookingCreate(BaseModel):
    first_name: str = Field(..., max_length=80)
    last_name: str = Field(..., max_length=80)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=30)
    service: Optional[str] = Field(None, max_length=120)
    preferred_date: Optional[str] = None
    preferred_time: Optional[str] = None
    message: Optional[str] = None

    @field_validator("first_name", "last_name")
    @classmethod
    def no_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Field cannot be blank")
        return v.strip()


class BookingStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(pending|confirmed|cancelled)$")


class BookingOut(BookingCreate):
    id: int
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}


# ───────────────────────── Contact ──────────────────────────


class ContactCreate(BaseModel):
    first_name: str = Field(..., max_length=80)
    last_name: str = Field(..., max_length=80)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=30)
    subject: Optional[str] = Field(None, max_length=200)
    message: str = Field(..., min_length=5)

    @field_validator("first_name", "last_name", "message")
    @classmethod
    def no_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Field cannot be blank")
        return v.strip()


class ContactOut(ContactCreate):
    id: int
    is_read: bool
    created_at: datetime

    model_config = {"from_attributes": True}


# ───────────────────────── Testimonials ─────────────────────


class TestimonialCreate(BaseModel):
    name: str = Field(..., max_length=120)
    role: Optional[str] = Field(None, max_length=120)
    text: str = Field(..., min_length=10)
    rating: int = Field(5, ge=1, le=5)
    is_featured: bool = False


class TestimonialOut(TestimonialCreate):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


# ───────────────────────── Generic ──────────────────────────


class MessageResponse(BaseModel):
    message: str
