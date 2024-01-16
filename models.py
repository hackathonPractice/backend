from database import Base
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(String)
    dateOfBirth = Column(String)
    role = Column(String)

