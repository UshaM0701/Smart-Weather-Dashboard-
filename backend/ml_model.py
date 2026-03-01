import numpy as np
from sklearn.linear_model import LinearRegression

# Sample historical temperature data
days = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
temps = np.array([30, 31, 29, 32, 33])

model = LinearRegression()
model.fit(days, temps)

def predict_temperature():
    next_day = np.array([[6]])
    prediction = model.predict(next_day)
    return round(float(prediction[0]), 2)
