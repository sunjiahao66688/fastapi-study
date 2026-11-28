from fastapi import APIRouter
from typing import Union,Optional

app02 = APIRouter()

@app02.get("/jobs/{kd}")
async def get_jobs(kd:str,xl:Union[None,str]=None,gj:Optional[str]=None):
    return {
        "kd":kd,
        "xl":xl,
        "gj":gj,
    }