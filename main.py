from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def login():
    return {"user":"sribalaji", "format":"json"}


@app.get('/about')
def about():
    return {"profile":"sribalaji", "format":"json"}