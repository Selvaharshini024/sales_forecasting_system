## Overview
This project is a production-ready time series forecasting system designed to predict future sales using historical data. It integrates data preprocessing, feature engineering, multiple model training, evaluation, and deployment using a REST API.
The system forecasts next 8 weeks (56 days) of sales per state, handling real-world challenges such as missing values, irregular time intervals, and seasonality.

## Objectives
- Train multiple forecasting models
- Compare model performance using evaluation metrics
- Automatically select the best model
- Handle missing data and time gaps
- Capture trend and seasonality patterns
- Deploy predictions via REST API

## Dataset Description
The dataset contains the following fields:
- State – Geographic region
- Date – Timestamp of sales
- Total – Sales value
- Category – Product category

## Key Challenges
- Missing dates
- Missing values
- Irregular time intervals
- Multi-state forecasting requirement

## Data Preprocessing
- Converted Date column to datetime format
- Sorted data by state and date
- Handled missing values using forward fill
- Ensured continuous date sequence per state
- Removed invalid or null records

## Feature Engineering

### Lag Features
- t-1, t-7, t-30

### Rolling Statistics
- 7-day rolling mean
- 7-day rolling standard deviation

### Date Features
- Day of week
- Month

These features help capture:
- Short-term dependencies
- Weekly patterns
- Seasonality trends

## Models Implemented
- ARIMA – Statistical forecasting model
- Prophet – Handles trend and seasonality
- XGBoost – Machine learning model using engineered features
- LSTM – Deep learning sequence model

## Model Evaluation
Metric used:
- Mean Absolute Error (MAE)

Results:
- ARIMA → High error
- Prophet → Moderate error
- XGBoost → Lowest error

Final Model:
- XGBoost selected as best model

## Forecasting Output
- Predicts next 8 weeks (56 days)
- Captures trend and seasonality patterns

## API Deployment (FastAPI)

### Endpoints
- / → Health check
- /predict → Returns forecast

### Sample Response
{
  "forecast": [12000, 13500, 14200]
}

## Project Architecture
Data → Preprocessing → Feature Engineering → Model Training → Evaluation → Best Model → API Deployment

## Project Structure
forecasting-system/
│
├── data/
├── src/
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
│   ├── evaluate.py
│
├── models/
├── main.py
├── app.py
├── requirements.txt

## How to Run

### Install dependencies
pip install -r requirements.txt

### Train models
python main.py

### Run API
uvicorn app:app --reload

### Access API documentation
http://127.0.0.1:8000/docs


## Challenges Faced
- Handling incorrect file formats (Excel issues)
- Missing column mismatches
- Time series indexing issues
- Long training time for Prophet and LSTM

## Future Scope
- State-wise model optimization
- Hyperparameter tuning
- Cloud deployment (AWS/GCP)
- Dashboard visualization
- Real-time data streaming

## Key Learnings
- Importance of feature engineering in time series
- Difference between statistical and ML models
- Handling real-world messy data
- Deploying ML models using APIs
- Building scalable backend systems

## Conclusion
This project demonstrates a complete end-to-end machine learning pipeline for time series forecasting. It integrates preprocessing, feature engineering, model training, evaluation, and deployment into a scalable backend system suitable for real-world business applications.
