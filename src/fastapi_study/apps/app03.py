from fastapi import APIRouter
from pydantic import BaseModel,Field,validator
from typing import List
from datetime import date

app03 = APIRouter()

class Addr(BaseModel):
    province:str
    city:str

class User(BaseModel):
    name:str = "XiaoMing"
    age:int = Field(default=14,gt=0,lt=100)
    birth:date
    friends:List[int] = []
    phone:str = Field(pattern="\d{11}")
    addr:Addr
    @validator("name")
    def name_must_be_alpha(cls,value):
        assert value.isalpha(),"name must be alpha"
        return value
        
class Data(BaseModel):
    data:List[User]
    
@app03.post("/user")
async def user(user:User):
    return user
@app03.post("/data")
async def data(data:Data):
    return data