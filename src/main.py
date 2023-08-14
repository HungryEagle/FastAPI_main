from fastapi import FastAPI
from .routes import items

app = FastAPI()
app.include_router(items.router)


@app.get("/")
async def root():
    return {"message": "Hello Main Application!"}