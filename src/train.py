from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
from xgboost import XGBRegressor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train_arima(train):
    model = ARIMA(train['sales'], order=(5,1,0))
    return model.fit()

def train_prophet(train):
    df = train[['date','sales']]
    df.columns = ['ds','y']
    model = Prophet()
    model.fit(df)
    return model

def train_xgb(train, features):
    model = XGBRegressor()
    model.fit(train[features], train['sales'])
    return model

def train_lstm(train, features):
    X = train[features].values
    y = train['sales'].values

    X = X.reshape((X.shape[0], 1, X.shape[1]))

    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(1, X.shape[2])))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=10, verbose=1)

    return model