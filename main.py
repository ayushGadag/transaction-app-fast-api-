from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"welcome 🚀"}

@app.post("/transactions")
def create_transaction(amount:float):
    return{
        "status":"success",
        "amount_recived": amount
    }