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
    api_key = "a1394bff6f7c9a8bcc6e1812bc12d627"
    url_complete = f"{url}?q={city}&units=metric&appid={api_key}"
    response = requests.get(url_complete)
    data = json.loads(response.text)
    temperature = data["main"]["temp"]
    return jsonify({"city": city, "temperature": temperature})

if __name__ == "__main__":
    app.run()
