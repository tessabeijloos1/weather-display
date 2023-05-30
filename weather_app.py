from flask import Flask, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_weather():
    city = "Den Bosch"
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "YOUR_API_KEY"
    url_complete = f"{url}?q={city}&units=metric&appid={api_key}"
    response = requests.get(url_complete)
    data = json.loads(response.text)
    temperature = data["main"]["temp"]
    return jsonify({"city": city, "temperature": temperature})

if __name__ == "__main__":
    app.run()
