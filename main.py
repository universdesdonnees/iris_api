from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the trained model
model = joblib.load("iris_model.joblib")

# Define a Pydantic model for input validation
class InputData(BaseModel):
    data: list[float]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def predict(input_data: InputData):
    # Validate that the input data has the correct shape (4 features for iris)
    if len(input_data.data) != 4:
        raise HTTPException(status_code=400, detail="Input data must have exactly 4 features.")
    # Convert input data to a numpy array and reshape it for the model
    try:
        input_array = np.array(input_data.data).reshape(1, -1)
        prediction = model.predict(input_array)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in prediction: {str(e)}")
