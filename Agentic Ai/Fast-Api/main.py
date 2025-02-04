from fastapi import FastAPI

app = FastAPI()

@app.get("/login")

def hello_fastapo():
    return {"Hello": "World"}


@app.get("/login username")

def hello_fastapi1():
    return {"Hello": "World"}
