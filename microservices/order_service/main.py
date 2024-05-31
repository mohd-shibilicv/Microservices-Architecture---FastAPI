import httpx
from fastapi import FastAPI, HTTPException, Depends

from .models import OrderModel
from ..user_service.models import UserModel


app = FastAPI()

orders_db = []


async def get_user(user_id: int) -> UserModel:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:8000/users/{user_id}/")
        response.raise_for_status()
        return UserModel(**response.json())
    

@app.post("/orders/", response_model=OrderModel)
async def create_order(order: OrderModel, user: UserModel = Depends(get_user)):
    orders_db.append(order)
    return order


@app.get("/orders/{order_id}/", response_model=OrderModel)
async def get_order(order_id: int):
    for order in orders_db:
        if order.id == order_id:
            return order
        raise HTTPException(status_code=404, detail='Order not found')
