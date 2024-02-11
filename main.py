# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Simple API"}



@app.get("/ep-1")
async def root():
    return {"message": "Simple API-1"}

@app.get("/ep-2")
async def root():
    return {"message": "Simple API-2"}