# app/ml_model/price_prediction.py

import joblib

# Load the pre-trained model
model = joblib.load("price_predictor.pkl")

def predict_price(features):
    # Predict price using the trained model
    prediction = model.predict([features])
    return prediction[0]
