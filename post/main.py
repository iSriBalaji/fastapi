from fastapi import FastAPI, Depends, status, Response, HTTPException
from post.schema import Post
from post import model
from post.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# we are creating all the database tables in the sqllite when there is no table in it
model.Base.metadata.create_all(engine)

# @app.post("/create", status_code=201)
# we can import status and put the status code directly here like this(below)
@app.post("/create", status_code=status.HTTP_201_CREATED)
def create(request: Post, db: Session = Depends(get_db)):
    new_post = model.Post(title = request.title, post = request.post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/see")
def select(db: Session = Depends(get_db)):
    posts = db.query(model.Post).all()
    return posts

@app.get("/post/{id}", status_code=status.HTTP_200_OK)
def specific_post(id, response = Response, db: Session = Depends(get_db)):
    post = db.query(model.Post).filter(model.Post.id == id).first()
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog Post of {id} is not present in the db")
    return post