# copied from fastapi sqlalchemy documentations//
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    post = Column(String)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key= True)
    name = Column(String)
    email = Column(String)
    password = Column(String)