# app/ml_model/price_prediction.py

import joblib
import numpy as np

# Load the pre-trained model (you should train it with historical price data)
model = joblib.load("price_predictor.pkl")

def predict_price(features):
    prediction = model.predict([features])
    return prediction[0]
