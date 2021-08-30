from fastapi import FastAPI 

from typing import List
from fastapi import Depends , FastAPI ,HTTPException

from . models import bidding, order,products,user 
from .config.db import SessionLocal,engine

from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
