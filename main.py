from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

class OdooWebhook(BaseModel):
    _action: str
    _id: int
    _model: str

app = FastAPI()

@app.post("/")
async def receive_webhook(webhook: OdooWebhook):
    print(f"Received webhook for model: {webhook._model} with id: {webhook._id}")
    return {"status": "received"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
