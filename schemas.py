from datetime import date

from typing import List
from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    id:int
    accessToken: str
    token_type: str
    email:EmailStr
    role:str
    phone:str
    name:str
    dateOfBirth:date


class TokenData(BaseModel):
    id:int


class payload(BaseModel):
    id:int
    email:EmailStr
    role:str
    phone:str
    name:str
    dateOfBirth:date
    

    class Config:
        orm_mode = True


class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str
    dateOfBirth: date
    role: str
   

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    dateOfBirth: date
    role: str
   

    class Config:
        orm_mode = True


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    