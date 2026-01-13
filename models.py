# SQLAlchemy ke columns aur data types
from sqlalchemy import Column, Integer, Float, String

# Base class jisse saare DB tables inherit honge
from database import Base

# Pydantic model ke liye
from pydantic import BaseModel

# Optional fields ke liye (PATCH use-case)
from typing import Optional


# 🔹 SQLAlchemy Model (DATABASE TABLE)
class TransactionDB(Base):
    __tablename__ = "transactions"   # DB me table ka naam

    id = Column(Integer, primary_key=True, index=True)  # Auto-increment PK
    amount = Column(Float, nullable=False)              # Transaction amount
    type = Column(String, nullable=False)               # credit / debit


# 🔹 Pydantic Model (UPDATE REQUEST BODY)
class TransactionUpdate(BaseModel):
    # Optional = value aa bhi sakti hai ya nahi bhi
    # PATCH API ke liye perfect
    amount: Optional[float] = None
    type: Optional[str] = None
