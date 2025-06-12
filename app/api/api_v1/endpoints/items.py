from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}}
)

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@router.get("/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "query": q}

@router.post("/")
async def create_item(item: Item):
    return item

