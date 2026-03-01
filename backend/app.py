from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "8d9fdc35bb1a7f9ff30aa79719689be9"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    city = data.get("city")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get("cod") != 200:
        return jsonify({"error": "City not found!"})

    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]

    # For demo AQI (real AQI needs separate API)
    aqi = round(humidity / 2)

    advisory = ""

    if temperature > 35:
        advisory += "High temperature. Stay hydrated. "

    if humidity > 75:
        advisory += "High humidity levels. "

    if aqi > 100:
        advisory += "Poor air quality. Avoid outdoor activity."

    if advisory == "":
        advisory = "Weather conditions are normal."

    return jsonify({
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
        "aqi": aqi,
        "advisory": advisory
    })

if __name__ == "__main__":
    app.run(debug=True)