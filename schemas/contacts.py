# Schemas of Contact in Application - Pydantic
from typing import Optional

from fastapi import Path
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


class ContactCreate(ContactBase):
    first_name: str = Path(min_length=3, max_length=100)
    last_name: str = Path(min_length=3, max_length=100)
    phone_number: str = Path(min_length=11, max_length=11, regex=r'^09([0-9]){9}$')


class ContactUpdate(ContactBase):
    first_name: Optional[str] = Field(None, min_length=3, max_length=100)
    last_name: Optional[str] = Field(None, min_length=3, max_length=100)
    phone_number: Optional[str] = Field(None, min_length=11, max_length=11, pattern=r'^09([0-9]){9}$')


class Contact(ContactBase):
    id: int

    class Config:
        from_attributes = True
