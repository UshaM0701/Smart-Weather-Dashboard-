Smart Weather Dashboard

An AI-powered weather dashboard that provides real-time weather data, air quality insights, and intelligent climate risk predictions in a clean and user-friendly interface.

🚀 Features

🌡 Real-time temperature and weather conditions

🌬 Air Quality Index (AQI) monitoring

📊 Clear weather trend visualization

🔄 Refresh button for updated data

🤖 Basic predictive risk model (heat / pollution risk)

🧠 Beginner-friendly ML integration

🏙 Designed for scalable use in Tier-2/Tier-3 cities

🛠 Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

Machine Learning: Scikit-learn

Data Handling: Pandas, NumPy

API: OpenWeatherMap API

📂 Project Structure
smart_weather_app/
│
├── backend/          # Flask backend
├── model/            # ML model files
├── data/             # Dataset files
├── static/           # CSS, JS
├── templates/        # HTML files
├── requirements.txt
└── README.md


⚙️ Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/UshaM0701/Smart-Weather-Dashboard-.git
cd smart_weather_app
2️⃣ Create virtual environment
python -m venv env

Activate it:

Windows

env\Scripts\activate

Mac/Linux

source env/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add your API key

Create a .env file or add your OpenWeather API key inside backend config.

Example:

API_KEY=your_api_key_here
5️⃣ Run the application
python app.py

Then open:

http://127.0.0.1:5000/

🧠 Methodology

Fetch real-time weather data using API.

Process temperature, humidity, AQI.

Feed features into trained ML model.

Predict climate risk level.

Display results with visual graphs.

Provide simple explainable alerts to users.

📊 Future Improvements

Hyper-local street-level prediction

Real-time explainable AI insights

SMS / mobile notifications

Historical data trend analysis

Deployment to cloud (Render / AWS / Railway)

🎯 Project Goal

To build an affordable and deployable smart weather prediction system that simplifies climate risk awareness for everyday users.

👩‍💻 Author

Usha M
GitHub: https://github.com/UshaM0701


