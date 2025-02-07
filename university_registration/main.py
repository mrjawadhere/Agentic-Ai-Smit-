from fastapi import FastAPI
from routes import router

app = FastAPI(title="University Registration API")

# Include routes
app.include_router(router)

# Run the application using: uvicorn main:app --reload
