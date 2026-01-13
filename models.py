from sqlalchemy import Column, Integer, Float, String
from database import Base
from pydantic import BaseModel
from typing import Optional

class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)

class  TransactionUpdate(BaseModel):
    amount:Optional[float]=None
    type:Optional[str]=None