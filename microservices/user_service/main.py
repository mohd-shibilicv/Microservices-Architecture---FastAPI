from fastapi import FastAPI, HTTPException

from .models import UserModel


app = FastAPI()

users_db = []


@app.post("/users/", response_model=UserModel)
async def create_user(user: UserModel):
    users_db.append(user)
    return user


@app.get("/users/{user_id}/", response_model=UserModel)
async def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
        raise HTTPException(status_code=404, detail="User not found")
