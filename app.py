from fastapi import FastAPI
import pickle

app = FastAPI()

model = pickle.load(open("models/best_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/predict")
def predict():
    forecast = model.forecast(steps=56)
    return {"forecast": forecast.tolist()}