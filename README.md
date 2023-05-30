# Weather Temperature Display

This project is a temperature display application that shows the current temperature in Den Bosch using data retrieved from the OpenWeather API. The temperature is updated every second, providing real-time information.

## Features
Displays the current temperature in Den Bosch.
Updates the temperature every second.
Fetches temperature data from the OpenWeather API.
## Prerequisites
To run this project locally, you need to have the following:

Python 3 installed on your machine.
An API key from OpenWeather. You can obtain a free API key by signing up at OpenWeather.
## Setup
Follow these steps to set up the project:

Clone the repository:

bash:  ` git clone https://github.com/tessabeijloos1/test.git `

Navigate to the project directory. Install the required dependencies:


` pip install -r requirements.txt `


Open the **weather_app.py** file and replace the `api_key` variable in the get_weather() function with your own OpenWeather API key.


## Usage
Run the following command to start the temperature display application:

` python weather_app.py `

Then change the server endpoint in the **scheduler.html** file to your server endpoint.
Open another terminal and cd into the project. Run: 

` open scheduler.html ` 

This will open a new tab in your default browser.

The application will fetch the current temperature in Den Bosch and display it on the screen. You can also choose to change the city to any city you want to be displayed. The temperature will be updated every second (due to the scheduler).

Press Ctrl + C to stop the application.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.
