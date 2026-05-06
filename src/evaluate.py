from sklearn.metrics import mean_absolute_error

def evaluate(test, predictions):
    scores = {}
    for name, pred in predictions.items():
        scores[name] = mean_absolute_error(test['sales'][:len(pred)], pred)
    return scores