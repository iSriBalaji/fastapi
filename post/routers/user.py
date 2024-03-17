from typing import List
from fastapi import APIRouter, FastAPI, Request, Response, Depends, status, HTTPException
from ..schema import ShowPost, ShowUser, User, Post, PostBase
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from .. import model

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)




@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    encrypt_password = Hash.encrypt(request.password)
    new_user = model.User(name = request.name, email = request.email, password = encrypt_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def show_user(id, db: Session = Depends(get_db)):
    user_data = db.query(model.User).filter(model.User.id == id).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found//")
        return {"status": "No post with the ID found"}
    return user_data