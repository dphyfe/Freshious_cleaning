from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/services", tags=["Services"])


@router.get("/", response_model=List[schemas.ServiceOut])
def list_services(db: Session = Depends(get_db)):
    """Return all active services."""
    return db.query(models.Service).filter(models.Service.is_active == True).all()


@router.get("/{service_id}", response_model=schemas.ServiceOut)
def get_service(service_id: int, db: Session = Depends(get_db)):
    """Return a single service by ID."""
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    return service


@router.post("/", response_model=schemas.ServiceOut, status_code=status.HTTP_201_CREATED)
def create_service(payload: schemas.ServiceCreate, db: Session = Depends(get_db)):
    """Create a new service entry."""
    existing = db.query(models.Service).filter(models.Service.slug == payload.slug).first()
    if existing:
        raise HTTPException(status_code=400, detail="A service with this slug already exists")
    service = models.Service(**payload.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@router.patch("/{service_id}", response_model=schemas.ServiceOut)
def update_service(service_id: int, payload: schemas.ServiceUpdate, db: Session = Depends(get_db)):
    """Partially update a service."""
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(service, field, value)
    db.commit()
    db.refresh(service)
    return service


@router.delete("/{service_id}", response_model=schemas.MessageResponse)
def delete_service(service_id: int, db: Session = Depends(get_db)):
    """Delete a service by ID."""
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    db.delete(service)
    db.commit()
    return {"message": f"Service '{service.name}' deleted successfully"}


from ..models import Service
from ..schemas import ServiceCreate, ServiceOut, ServiceUpdate, MessageResponse

router = APIRouter(prefix="/services", tags=["Services"])


@router.get("/", response_model=List[ServiceOut], summary="List all active services")
def list_services(db: Session = Depends(get_db)):
    return db.query(Service).filter(Service.is_active == True).all()


@router.get("/{slug}", response_model=ServiceOut, summary="Get a service by slug")
def get_service(slug: str, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.slug == slug).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@router.post("/", response_model=ServiceOut, status_code=status.HTTP_201_CREATED, summary="Create a service")
def create_service(payload: ServiceCreate, db: Session = Depends(get_db)):
    if db.query(Service).filter(Service.slug == payload.slug).first():
        raise HTTPException(status_code=409, detail="A service with this slug already exists")
    service = Service(**payload.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@router.patch("/{service_id}", response_model=ServiceOut, summary="Update a service")
def update_service(service_id: int, payload: ServiceUpdate, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(service, field, value)
    db.commit()
    db.refresh(service)
    return service


@router.delete("/{service_id}", response_model=MessageResponse, summary="Delete a service")
def delete_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    db.delete(service)
    db.commit()
    return {"message": f"Service '{service.name}' deleted successfully"}
