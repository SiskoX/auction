from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    phonenumber= Column(Integer)
    
    # items = relationship("Item", back_populates="owner")



class PaymentInfo(BaseModel):
    __tablename__ = "paymentinfo"
    id  = Column (Integer, primary_key=True, index=True)
    name = Column(String )
    phone = Column(int ,unique=True ,index=True )
    location = Column(String )


class ShipppingAddress(BaseModel):
    __tablename__ = "shippingaddress"
    id = Column(Integer, primary_key=True,unique=True)
    address1 = Column (String )
    adress2 = Column (String)
    postalcode = Column(Integer)
    city  = Column(String )
    country = Column(String)
    