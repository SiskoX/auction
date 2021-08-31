from schemas import biddingschemas,ordschemas,productschemas,userschemas

from fastapi import FastAPI

app = FastAPI()

@app.post("/user/", response_model=  userschemas.UserSchemas)
async def create_user(user:userschemas.UserSchemas):
    return user 

@app.get ("/user/{id}/",response_model=userschemas.UserSchemas)
async def get_usr (id:str):
    return id 