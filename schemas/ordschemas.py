from fastapi import FastAPI
from pyddantic import BaseModel

from datetime import datetime 
 

class OrderSchemas(BaseModel):
    id : int 
    name: str 
    condtion_description: str
    photo : str 
    starting_price : float 
    buy_it_now_price : float 
    reserve_price : float
    quantity : int 
    duration : datetime 
    item_descrption : str 

class Shipping_Address (BaseModel):
    address : str 
    phon