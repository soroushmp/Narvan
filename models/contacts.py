# Contact Table For Database Initialization
from sqlalchemy import Column, String, Integer

from database import Base


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
