import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("../data/wpa.csv.csv")

print("Columns in dataset:")
print(df.columns)

# -----------------------------
# We will use:
# X = dayofyear
# y = temp (average temperature)
# -----------------------------

X = df[['dayofyear']]
y = df['temp']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("weather_model.pkl", "wb"))

print("Model trained successfully and saved!")
