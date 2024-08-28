# main.py

from fastapi import FastAPI
from app.api.endpoints import files

app = FastAPI()
app.include_router(files.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}