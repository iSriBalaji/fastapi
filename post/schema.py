from pydantic import BaseModel

class Post(BaseModel):
    title: str
    post: str

class ShowPost(BaseModel):
    title: str
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
    class Config():
        orm_model = True