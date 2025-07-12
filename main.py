from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

class OdooWebhook(BaseModel):
    _action: str
    _id: int
    _model: str
    amount_paid: Optional[float] = None
    amount_residual: Optional[float] = None
    amount_total_words: Optional[str] = None
    display_name: Optional[str] = None
    highest_name: Optional[str] = None
    id: int
    invoice_filter_type_domain: Optional[bool] = None
    invoice_line_ids: Optional[List[int]] = None
    is_lab_invoice: Optional[bool] = None
    move_type: Optional[str] = None
    type_name: Optional[str] = None

app = FastAPI()

@app.post("/")
async def receive_webhook(webhook: OdooWebhook):
    print(f"Received webhook for model: {webhook._model} with id: {webhook._id}")
    return {"status": "received"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
