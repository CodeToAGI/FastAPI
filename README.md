# CodeToAGI — Episode 55 Challenge

## 🎯 Challenge: Add Confidence Score to PredictAPI

**Task**: Extend the PredictAPI by adding a `confidence` field to the response.

### What to Implement
- Update the response model (`PredictionResponse`) to include `confidence: float`
- Return a confidence score (between 0 and 1) alongside the prediction
- Verify it appears correctly in the automatic `/docs` page

### How to Run

```bash
# 1. Activate environment
myenv\Scripts\activate

# 2. Install FastAPI + Uvicorn
pip install fastapi uvicorn pydantic

# 3. Run the API
python challenge_ep55.py
