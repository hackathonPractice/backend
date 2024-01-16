import models
import schemas
import utils
import oauth2
import database
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/signup", response_model=schemas.UserOut,
             status_code=201)
def signup(user: schemas.UserSignup, db: Session = Depends(database.get_db)):
    user.password = utils.hash(user.password)
    user = models.User(**user.model_dump())
    user.role = "USER"
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/signin", response_model=schemas.Token,
             status_code=200)

def signin(userCredentials: schemas.UserSignIn, db: Session = Depends(database.get_db)): 
    user = db.query(models.User).filter(models.User.email == userCredentials.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="error")
    if not utils.verify(userCredentials.password, user.password):
        raise HTTPException(status_code=400, detail="error")
    
    accessToken = oauth2.createAccessToken(
        data={"id": user.id, "email": user.email, "role": user.role, "phone": user.phone, "name": user.name, "dateOfBirth": user.dateOfBirth})
    return schemas.Token(id=user.id, accessToken=accessToken, token_type="bearer", email=user.email, role=user.role, phone=user.phone, name=user.name, dateOfBirth=user.dateOfBirth)

    