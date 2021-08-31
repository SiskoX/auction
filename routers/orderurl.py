from models.order import ShippingAddress
from schemas import ordschemas

from fastapi import FastAPI 

app = FastAPI()

@app.post("/order/", response_model = ordschemas.OrderSchemas)
async def create_order (order: ordschemas.OrderSchemas):
    return order

@app.post("/shipping_address/", response_model = ordschemas.Shipping_Address)
async def create_shipping_info (shipping_address : ordschemas.Shipping_Address):

    return shipping_address

@app.get ("/shipping_details/{shipping_details}", response_model=ordschemas.Shipping_Address)
async def get_shipping_details(shipping_details: ordschemas.Shipping_Address):

    return shipping_details
@app.get ("/order_details/{ord_id}", response_model = ordschemas.OrderSchemas)
async def get_order (ord_id = ordschemas.OrderSchemas):
    return or