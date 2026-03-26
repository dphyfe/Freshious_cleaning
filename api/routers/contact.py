from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post("/", response_model=schemas.ContactOut, status_code=status.HTTP_201_CREATED)
def submit_contact(payload: schemas.ContactCreate, db: Session = Depends(get_db)):
    """Submit a contact / enquiry message."""
    msg = models.ContactMessage(**payload.model_dump())
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


@router.get("/", response_model=List[schemas.ContactOut])
def list_messages(
    unread_only: bool = Query(False),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    """List all contact messages, optionally filtered to unread only."""
    q = db.query(models.ContactMessage)
    if unread_only:
        q = q.filter(models.ContactMessage.is_read == False)
    return q.order_by(models.ContactMessage.created_at.desc()).offset(skip).limit(limit).all()


@router.get("/{message_id}", response_model=schemas.ContactOut)
def get_message(message_id: int, db: Session = Depends(get_db)):
    """Retrieve a single contact message by ID."""
    msg = db.query(models.ContactMessage).filter(models.ContactMessage.id == message_id).first()
    if not msg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    return msg


@router.patch("/{message_id}/read", response_model=schemas.ContactOut)
def mark_as_read(message_id: int, db: Session = Depends(get_db)):
    """Mark a contact message as read."""
    msg = db.query(models.ContactMessage).filter(models.ContactMessage.id == message_id).first()
    if not msg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    msg.is_read = True
    db.commit()
    db.refresh(msg)
    return msg


@router.delete("/{message_id}", response_model=schemas.MessageResponse)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    """Delete a contact message."""
    msg = db.query(models.ContactMessage).filter(models.ContactMessage.id == message_id).first()
    if not msg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    db.delete(msg)
    db.commit()
    return {"message": "Message deleted successfully"}


from ..models import ContactMessage
from ..schemas import ContactCreate, ContactOut, MessageResponse

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post("/", response_model=ContactOut, status_code=status.HTTP_201_CREATED, summary="Submit a contact message")
def submit_contact(payload: ContactCreate, db: Session = Depends(get_db)):
    msg = ContactMessage(**payload.model_dump())
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


@router.get("/", response_model=List[ContactOut], summary="List all contact messages")
def list_messages(
    unread_only: bool = Query(False, description="Return only unread messages"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    query = db.query(ContactMessage)
    if unread_only:
        query = query.filter(ContactMessage.is_read == False)
    return query.order_by(ContactMessage.created_at.desc()).offset(skip).limit(limit).all()


@router.get("/{message_id}", response_model=ContactOut, summary="Get a contact message by ID")
def get_message(message_id: int, db: Session = Depends(get_db)):
    msg = db.query(ContactMessage).filter(ContactMessage.id == message_id).first()
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    msg.is_read = True
    db.commit()
    db.refresh(msg)
    return msg


@router.delete("/{message_id}", response_model=MessageResponse, summary="Delete a contact message")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    msg = db.query(ContactMessage).filter(ContactMessage.id == message_id).first()
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(msg)
    db.commit()
    return {"message": f"Message #{message_id} deleted successfully"}
