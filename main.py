from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def login():
    return {"user":"sribalaji", "format":"json"}


@app.get('/about')
def about():
    return {"profile":"sribalaji", "format":"json"}

@app.get('/heat/{location}')
def temp(location):
    return {"data": {"temp": "23", "uv_index": "2", "location": location}}

#path parameters
@app.get('/post/{id}/count')
def likes(id):
    if(id==2):
        return {"data": "two"}
    elif(id==3):
        return {"data": "three"}
    else:
        return {"data": id}

@app.get('/date/{month}')
def temp(month: int):
    return {"data": {"month":month, "comment": " pleasant"}}

# query parameters
@app.get('/event/')
def temp(date:str = 'default_date', comment:int = 10, point_break: Optional[str] = None):
    return {"event_json": {"date":date, "comment": comment, "point_break": point_break}}

# if any variable defined in the path it will take it as a path parameter and all other variables are taken as query parameters
@app.get('/qpath/{id}')
def here(id:int, date:str = 'both query and path params'):
    return {"data": {"id": id, "date_query": date}}

class FB_Post(BaseModel):
    id: int
    content: str
    comment: str
    likes: int
    others: Optional[str]

# post method - test it in the swagger uibr
@app.post('/create/')
def create_post():
    return "created"

@app.post('/req/')
def blog(request: FB_Post):
    # return request
    return {"data":f"post is created {request.content}"}
    pass

# we can directly > using python F5
# if __name__ == "__main__":
#     uvicorn.run(app, host = "127.0.0.1", port = 8023)

