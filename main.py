from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Transaction(BaseModel): #data iherit from basemodel this is class /BaseModel = Parent


    amount: float
    type: str

@app.post("/transactions")
def create_transaction(transaction: Transaction): ##Transaction : type{transaction} 
    return {
        "status": "success",
        "amount_received": transaction.amount,
        "type": transaction.type
    }
