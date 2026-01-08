from fastapi import FastAPI , HTTPException # 'HTTPException' is a class in Fast-API
from pydantic import BaseModel , Field # 'Feild' is function inside a paydantic
from database import engine
import models
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from models import TransactionDB

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class Transaction(BaseModel): #data iherit from basemodel this is class /BaseModel = Parent
    amount: float = Field(..., gt=0,le=1000) #amount greater than zero must be / 0 or -10 will be rejected
    type: str

@app.post("/transactions")
def create_transaction(transaction: Transaction): ##Transaction : type{transaction} 
    if transaction.type not in ["credit", "debit"]:
        raise HTTPException(
            status_code=400,
            detail="transaction type must be 'debit' or a 'credit'"
        )
    return {
        "status": "success",
        "amount_received": transaction.amount,
        "type": transaction.type
    }
