from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import Account, Login
from database import get_db
from models import User
from hashing import Hash


router = APIRouter(prefix = "/accounts", tags= ["Accounts"])


@router.post("/sign-up")
def create_new_account(request: Account, db: Session = Depends(get_db)):
    new_user = User(name = request.name, email = request.email, password =  Hash.hashing(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/sign-in")
def sign_in(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == request.username).first()
    if not user:
        raise HTTPException(status_code= 404, detail= "Not a Registered User")

    if not Hash.verifying(request.password, user.password):
        raise HTTPException(status_code= 401, detail= "Incorrect Password")

    else:
        return "Login Successful"


