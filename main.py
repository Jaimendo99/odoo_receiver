from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class OdooWebhook(BaseModel):
    _action: str
    _id: int
    _model: str

app = FastAPI()

@app.post("/")
async def receive_webhook(webhook: OdooWebhook):
    print(f"Received webhook for model: {webhook._model} with id: {webhook._id}")
    return {"status": "received"}
