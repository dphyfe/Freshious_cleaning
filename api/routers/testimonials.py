from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/testimonials", tags=["Testimonials"])


@router.get("/", response_model=List[schemas.TestimonialOut])
def list_testimonials(
    featured_only: bool = Query(False),
    db: Session = Depends(get_db),
):
    """Return all testimonials, optionally only featured ones."""
    q = db.query(models.Testimonial)
    if featured_only:
        q = q.filter(models.Testimonial.is_featured == True)
    return q.order_by(models.Testimonial.created_at.desc()).all()


@router.get("/{testimonial_id}", response_model=schemas.TestimonialOut)
def get_testimonial(testimonial_id: int, db: Session = Depends(get_db)):
    """Return a single testimonial by ID."""
    t = db.query(models.Testimonial).filter(models.Testimonial.id == testimonial_id).first()
    if not t:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Testimonial not found")
    return t


@router.post("/", response_model=schemas.TestimonialOut, status_code=status.HTTP_201_CREATED)
def create_testimonial(payload: schemas.TestimonialCreate, db: Session = Depends(get_db)):
    """Add a new testimonial."""
    t = models.Testimonial(**payload.model_dump())
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


@router.patch("/{testimonial_id}/feature", response_model=schemas.TestimonialOut)
def toggle_featured(testimonial_id: int, db: Session = Depends(get_db)):
    """Toggle the featured flag on a testimonial."""
    t = db.query(models.Testimonial).filter(models.Testimonial.id == testimonial_id).first()
    if not t:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Testimonial not found")
    t.is_featured = not t.is_featured
    db.commit()
    db.refresh(t)
    return t


@router.delete("/{testimonial_id}", response_model=schemas.MessageResponse)
def delete_testimonial(testimonial_id: int, db: Session = Depends(get_db)):
    """Delete a testimonial."""
    t = db.query(models.Testimonial).filter(models.Testimonial.id == testimonial_id).first()
    if not t:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Testimonial not found")
    db.delete(t)
    db.commit()
    return {"message": "Testimonial deleted successfully"}


from ..models import Testimonial
from ..schemas import TestimonialCreate, TestimonialOut, MessageResponse

router = APIRouter(prefix="/testimonials", tags=["Testimonials"])


@router.get("/", response_model=List[TestimonialOut], summary="List testimonials")
def list_testimonials(
    featured_only: bool = Query(False, description="Return only featured testimonials"),
    db: Session = Depends(get_db),
):
    query = db.query(Testimonial)
    if featured_only:
        query = query.filter(Testimonial.is_featured == True)
    return query.order_by(Testimonial.created_at.desc()).all()


@router.get("/{testimonial_id}", response_model=TestimonialOut, summary="Get a testimonial by ID")
def get_testimonial(testimonial_id: int, db: Session = Depends(get_db)):
    t = db.query(Testimonial).filter(Testimonial.id == testimonial_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    return t


@router.post("/", response_model=TestimonialOut, status_code=status.HTTP_201_CREATED, summary="Add a testimonial")
def create_testimonial(payload: TestimonialCreate, db: Session = Depends(get_db)):
    t = Testimonial(**payload.model_dump())
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


@router.patch("/{testimonial_id}/feature", response_model=TestimonialOut, summary="Toggle featured status")
def toggle_featured(testimonial_id: int, db: Session = Depends(get_db)):
    t = db.query(Testimonial).filter(Testimonial.id == testimonial_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    t.is_featured = not t.is_featured
    db.commit()
    db.refresh(t)
    return t


@router.delete("/{testimonial_id}", response_model=MessageResponse, summary="Delete a testimonial")
def delete_testimonial(testimonial_id: int, db: Session = Depends(get_db)):
    t = db.query(Testimonial).filter(Testimonial.id == testimonial_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    db.delete(t)
    db.commit()
    return {"message": f"Testimonial #{testimonial_id} deleted successfully"}
