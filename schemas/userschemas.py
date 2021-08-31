from pydantic import BaseModel
from datetime import datetime

class UserSchemas(BaseModel):
    id : int
    first_name : str
    last_name : str
    email : str 
    address : 
    city : str
    created : datetime

class BillingAddress(BaseModel):
    id : int
    location: str
    phone_number : int
    address : str 
    city : str 


