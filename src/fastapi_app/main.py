from fastapi import FastAPI
from .models import Item
from .database import get_items

app = FastAPI()

@app.get("/items", response_model=list[Item])
async def read_items():
    items = get_items()
    return items