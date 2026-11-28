from fastapi import APIRouter

app01 = APIRouter()

@app01.get("/user/{user_id}")
async def get_user(user_id:int):
    return {"user_id":user_id}