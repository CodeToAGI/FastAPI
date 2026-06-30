"""
CodeToAGI — Episode 55 Challenge
Add a Confidence Score Endpoint to PredictAPI (FastAPI)
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="PredictAPI")

class InputData(BaseModel):
    value: float

# Challenge: Enhanced response model with confidence
class PredictionResponse(BaseModel):
    result: float
    confidence: float   # New field for challenge

@app.post("/predict", response_model=PredictionResponse)
async def predict(data: InputData):
    """Simple prediction endpoint"""
    # Simulate model prediction
    result = data.value * 2.5  # dummy calculation
    confidence = 0.87  # dummy confidence score (between 0-1)
    
    return {
        "result": round(result, 4),
        "confidence": confidence
    }

@app.get("/predict/{item_id}")
async def get_prediction(item_id: int):
    """Example path parameter endpoint"""
    return {
        "item_id": item_id,
        "message": f"Prediction for item {item_id}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
