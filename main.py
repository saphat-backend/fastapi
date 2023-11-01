from typing import Union
from enum import Enum

from fastapi import FastAPI
port=8001
app = FastAPI(port=port)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

class FoodEnum(str, Enum):
    pizza = "pizza"
    burger = "burger"
    taco = "taco"

@app.get("/food")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.pizza:
        return {
            "food_name:": "pizza",
            "message": "I like pizza",
        }
    if food_name.value == "taco":
        return {
            "food_name:": "taco",
            "message": "I like taco",
        }
    return {
        "food_name:": "burger",
        "message": "I like burger",
    }

fake_items_db = [
    {"item_name": "Foo", "price": 35},
    {"item_name": "Bar", "price": 10},
    {"item_name": "Baz", "price": 15},
]
@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]