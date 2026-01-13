from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database import engine, get_db
import models
from models import TransactionDB, TransactionUpdate


app = FastAPI()

# DB tables create
models.Base.metadata.create_all(bind=engine)


# ---------- Pydantic Model (CREATE) ----------
class Transaction(BaseModel):
    amount: float = Field(..., gt=0, le=1000)
    type: str


# ---------- POST : Create Transaction ----------
@app.post("/transactions")
def create_transaction(
    transaction: Transaction,
    db: Session = Depends(get_db)
):
    if transaction.type not in ["credit", "debit"]:
        raise HTTPException(
            status_code=400,
            detail="transaction type must be 'credit' or 'debit'"
        )

    new_txn = TransactionDB(
        amount=transaction.amount,
        type=transaction.type
    )

    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)

    return {
        "status": "saved",
        "id": new_txn.id,
        "amount": new_txn.amount,
        "type": new_txn.type
    }


# ---------- GET : All Transactions ----------
@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(TransactionDB).all()

    return [
        {
            "id": txn.id,
            "amount": txn.amount,
            "type": txn.type
        }
        for txn in transactions
    ]


# ---------- PATCH : Update Transaction ----------
@app.patch("/transactions/{txn_id}")
def update_transaction(
    txn_id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db)
):
    txn = db.query(TransactionDB).filter(
        TransactionDB.id == txn_id
    ).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    if data.amount is not None:
        txn.amount = data.amount

    if data.type is not None:
        if data.type not in ["credit", "debit"]:
            raise HTTPException(status_code=400, detail="Invalid transaction type")
        txn.type = data.type

    db.commit()
    db.refresh(txn)

    return {
        "status": "updated",
        "id": txn.id,
        "amount": txn.amount,
        "type": txn.type
    }

@app.delete("/transactions/{txn_id}")
def delete_transaction(
    txn_id: int,
    db: Session = Depends(get_db)
):
    txn = db.query(TransactionDB).filter(TransactionDB.id == txn_id).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(txn)
    db.commit()

    return {
        "status": "deleted",
        "id": txn_id
    }
