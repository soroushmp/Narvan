# Route Functions of Contact
from typing import List

from fastapi import Depends, HTTPException, APIRouter, status, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse

from dependencies import get_db
from models import contacts as models
from schemas import contacts as schemas

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    contacts = read_contacts(db)
    context = {"request": request, "contacts": contacts}
    return templates.TemplateResponse("index.html", context)


@router.post('/contacts/', response_model=schemas.Contact, status_code=status.HTTP_201_CREATED)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact = db.query(models.Contact).filter(models.Contact.phone_number == contact.phone_number).first()
    if db_contact:
        raise HTTPException(detail="Phone Number Already Exists", status_code=400)
    contact = models.Contact(first_name=contact.first_name, last_name=contact.last_name,
                             phone_number=contact.phone_number)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


@router.get('/contacts/', response_model=List[schemas.Contact])
def read_contacts(db: Session = Depends(get_db)):
    db_contact = db.query(models.Contact)
    if db_contact is None:
        raise HTTPException(detail="Contact Not Found", status_code=404)
    return db_contact


@router.get('/contacts/{contact_id}', response_model=schemas.Contact)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(detail="Contact Not Found", status_code=404)
    return db_contact


@router.put('/contacts/{contact_id}', response_model=schemas.Contact)
def update_contact(contact_id: int, contact: schemas.ContactUpdate, db: Session = Depends(get_db)):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(detail="Contact Not Found", status_code=404)

    contact_dict = contact.model_dump()
    if contact_dict.get('phone_number', None):
        phone_number_duplicate = db.query(models.Contact).filter(models.Contact.id != contact_id).filter(
            models.Contact.phone_number == contact_dict['phone_number']).first()
        if phone_number_duplicate:
            raise HTTPException(detail="Phone Number Already Exists", status_code=400)
    for key, value in contact_dict.items():
        if value:
            setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.delete('/contacts/{contact_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(detail="Contact Not Found", status_code=404)
    db.delete(db_contact)
    db.commit()
