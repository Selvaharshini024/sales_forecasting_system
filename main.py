from src.preprocess import load_data
from src.features import create_features
from src.train import train_arima, train_prophet, train_xgb
from src.evaluate import evaluate
import pickle

# Load data
df = load_data("data/sales.xlsx")

# Clean
# df = fill_missing_dates(df)

# Features
df = create_features(df)

# Split
train = df[df['date'] < '2023-01-01']
test = df[df['date'] >= '2023-01-01']

features = ['lag_1','lag_7','lag_30','rolling_mean_7','day_of_week','month']

# Train models
arima_model = train_arima(train)
prophet_model = train_prophet(train)
xgb_model = train_xgb(train, features)

# Predictions
pred_arima = arima_model.forecast(steps=56)
future = prophet_model.make_future_dataframe(periods=56)
forecast = prophet_model.predict(future)
pred_prophet = forecast['yhat'].tail(56)

pred_xgb = xgb_model.predict(test[features])

# Evaluate
predictions = {
    "ARIMA": pred_arima,
    "Prophet": pred_prophet,
    "XGBoost": pred_xgb
}

scores = evaluate(test, predictions)

print("Scores:", scores)

best = min(scores, key=scores.get)
print("Best model:", best)

# Save best model
pickle.dump(arima_model, open("models/best_model.pkl", "wb"))