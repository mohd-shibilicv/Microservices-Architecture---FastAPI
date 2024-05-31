from pydantic import BaseModel, Field


class OrderModel(BaseModel):
    id: int
    user_id: int
    product_name: str
    quantity: int = Field(..., gt=0)
