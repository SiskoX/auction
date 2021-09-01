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

    # items = relationship("Item", back_populates="owner")



class PaymentInfo(BaseModel):
    __tablename__ = "paymentinfo"
    id  = Column (Integer, primary_key=True, index=True)
    name = Column(String )
    phone = Column(int ,unique=True ,index=True )
    location = Column(String )
    