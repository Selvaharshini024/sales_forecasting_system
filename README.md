End-to-End Time Series Forecasting System with API 
 
ABSTRACT: 
This project presents an end-to-end time series forecasting system designed to predict future sales 
using historical data. The system integrates data preprocessing, feature engineering, multiple model 
training, and evaluation, followed by deployment using a REST API. Models including ARIMA, 
Prophet, XGBoost, and LSTM are implemented and compared using Mean Absolute Error (MAE). 
The best-performing model is automatically selected to forecast the next 8 weeks of sales. The 
solution is designed as a scalable backend system suitable for real-world applications. 
 
PROJECT OVERVIEW:
This project focuses on building a production-ready time series forecasting system to predict future 
sales using historical data. The system is designed to simulate a real-world backend service by 
incorporating data preprocessing, feature engineering, multiple model training, evaluation, and 
deployment through a REST API. 
The primary objective is to forecast next 8 weeks of sales for each state, while handling real-world 
data challenges such as missing values, irregular time intervals, and seasonality. 
 
OBJECTIVES: 
• Train multiple forecasting models 
• Compare model performance using evaluation metrics 
• Automatically select the best model 
• Handle missing data and time gaps 
• Capture trend and seasonality 
• Deploy predictions via REST API 
 
DATASET DESCRIPTION:
The dataset contains historical sales data with the following fields: 
• State – Geographic region 
• Date – Timestamp of sales 
• Total – Sales value 
• Category – Product category 
 
KEY CHALLENGES:
• Missing dates 
• Missing values 
• Irregular time intervals 
• Multi-state forecasting requirement 
 
DATA PREPROCESSING: 
• Converted Date column to datetime format 
• Sorted data by state and date 
• Handled missing values using forward filling 
• Ensured continuous date sequence per state 
• Removed invalid or null records 
 
FEATURE ENGINEERING:
Feature engineering played a crucial role in improving model performance. 
CREATED FEATURES: 
• Lag Features: 
o t-1, t-7, t-30 
• Rolling Statistics: 
o 7-day rolling mean 
o 7-day rolling standard deviation 
• Date Features: 
o Day of week 
o Month 
These features help capture: 
• Short-term dependencies 
• Weekly patterns 
• Seasonality trends 
 
MODELS IMPLEMENTED: 
The following models were trained and evaluated: 
1. ARIMA 
• Captures linear patterns in time series 
• Suitable for stationary data 
2. Prophet 
• Handles seasonality and trend effectively 
• Robust to missing data 
3. XGBoost 
• Machine learning model using engineered features 
• Captures non-linear relationships 
4. LSTM 
• Deep learning model for sequence prediction 
• Captures long-term dependencies 
 
MODEL EVALUATION: 
Models were evaluated using: 
• Mean Absolute Error (MAE) 
SAMPLE OUTPUT: 
ARIMA   → High error   
Prophet → Moderate error   
XGBoost → Lowest error  
FINAL SELECTION: 
  XGBoost was selected as the best model 
 
FORECASTING OUTPUT: 
• Generated predictions for next 8 weeks (56 days) 
• Captures both: 
• Trend 
• Seasonality 
 
API DEPLOYMENT: 
The best model is deployed using FastAPI. 
API ENDPOINTS: 
• / → Health check 
• /predict → Returns forecast 
 
Sample Response: 
{ 
  "forecast": [12000, 13500, 14200, ...] 
} 
 
PROJECT ARCHITECTURE: 
Data → Preprocessing → Feature Engineering → Model Training → Evaluation → Best Model → 
API Deployment 
 
PROJECT STRUCTURE: 
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
 
HOW TO RUN THE PROJECT:
Step 1: Install dependencies 
pip install -r requirements.txt 
Step 2: Train models 
python main.py 
Step 3: Run API 
uvicorn app:app --reload 
Step 4: Access API 
http://127.0.0.1:8000/docs 
 
CHALLENGES FACED: 
• Handling incorrect file formats (Excel issues) 
• Missing column names mismatch 
• Time series indexing issues 
• Model training time (Prophet, LSTM) 
 
FUTURE SCOPE: 
• Implement state-wise model training for better accuracy  
• Apply hyperparameter tuning for improved performance  
• Deploy using cloud platforms (AWS/GCP)  
• Add dashboard visualization for business insights  
• Integrate real-time data streaming 
 
KEY LEARNINGS:
• Importance of feature engineering in time series 
• Difference between statistical and ML models 
• Handling real-world messy data 
• Deploying ML models using APIs 
• Building scalable backend systems 
 
CONCLUSION: 
This project successfully demonstrates a complete end-to-end machine learning pipeline for time 
series forecasting. It integrates data preprocessing, feature engineering, model training, evaluation, 
and deployment into a scalable backend system. By comparing multiple models and selecting the 
best-performing one, the solution ensures accurate and reliable predictions. The deployment using 
FastAPI enables real-world usability, making this system suitable for business applications and 
decision-making processes. 
 
