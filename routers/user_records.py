from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import User
from schemas import ShowUser
from typing import List

router = APIRouter(prefix= "/users", tags= ["Users"])

@router.get("/", response_model= List[ShowUser])
def all_user(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    return all_users

@router.get("/{id}", response_model= ShowUser)
def specific_user(id, db: Session = Depends(get_db)):
    the_user = db.query(User).filter(User.id == id).first()

    if not the_user:
        raise HTTPException(status_code= 404, detail= f"User {id} doesn't exist")
    return the_user