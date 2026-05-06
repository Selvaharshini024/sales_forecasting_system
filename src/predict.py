def forecast_arima(model, steps=56):
    return model.forecast(steps=steps)