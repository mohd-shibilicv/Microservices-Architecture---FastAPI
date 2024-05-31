from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    is_active: bool = True


class OrderModel(BaseModel):
    id: int
    user_id: int
    product_name: str
    quantity: int = Field(..., gt=0)
