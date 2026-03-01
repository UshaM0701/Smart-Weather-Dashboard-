let chart;

function predictWeather() {

    const city = document.getElementById("cityInput").value;

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            city: city
        })
    })
    .then(response => response.json())
    .then(data => {

        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById("temp").innerText = data.temperature + " °C";
        document.getElementById("humidity").innerText = data.humidity + " %";
        document.getElementById("pressure").innerText = data.pressure + " hPa";
        document.getElementById("aqi").innerText = data.aqi;

        document.getElementById("advisoryText").innerText = data.advisory;

        createChart(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function refreshWeather() {
    predictWeather();
}

function createChart(data) {

    const ctx = document.getElementById('weatherChart').getContext('2d');

    if (chart) {
        chart.destroy();
    }

    chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Temperature', 'Humidity', 'Pressure', 'AQI'],
            datasets: [{
                label: 'Weather Metrics',
                data: [
                    data.temperature,
                    data.humidity,
                    data.pressure,
                    data.aqi
                ]
            }]
        },
        options: {
            responsive: true
        }
    });
}