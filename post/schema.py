from pydantic import BaseModel
from typing import List

class PostBase(BaseModel):
    title: str
    post: str

class Post(PostBase):
    class Config():
        orm_model = True

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    post: List[Post] = []
    class Config():
        orm_model = True

# after creating a relation ship in the orm models
# I can change the same in the response models to get that relationship
class ShowPost(BaseModel):
    title: str
    creator: ShowUser # make sure to use the same 'variable' here remember we names it as creator in the model
    class Config():
        orm_model = True