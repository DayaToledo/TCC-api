import os
import json
import pandas as pd
from src.scripts.pre_processor import get_x
from fastapi import FastAPI, HTTPException
import pickle

from . import schemas

app = FastAPI(
    title="API to analyze personality",
    description="API that implements an endpoint to analyze a person's personality based on their responses",
    version="1.0",
)

@app.post("/predict", response_model=schemas.Result, tags=['Analyze'])
def get_analyze_personality(questions: schemas.Questions):
    try:
        data = json.loads(questions.json())
        df = pd.DataFrame.from_dict(data, orient="index")
        df = df.T
        test_data = get_x(df)
        # print(test_data)
        model = pickle.load(open('src/data/models/model_LogisticRegression_responsible.pkl', 'rb'))
        prediction = model.predict(test_data)[0]
        # print(prediction)
        return { "Prediction": prediction }
    except Exception as error:
        print("An error ocurred.", error)
        raise HTTPException(status_code=500, detail="An error ocurred.")
