from fastapi import FastAPI

app = FastAPI() 


@app.get("/")
def get_root():
    print("Fucntion called")
    return {"message": "Hello World"}

@app.get("/login")  
def get_login():
    return {"message": "Login"}

@app.get("/signup")  
def get_signup():
    return {"message": "Signup"}