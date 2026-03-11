import tkinter as tk
import requests

# Default API key (built-in)
DEFAULT_API_KEY = "bb4becf1d2eb85e25b02e6a951faf1a1"

def get_weather():
    user_api_key = api_entry.get()
    city = city_entry.get()

    # Use default key if user didn't enter one
    if user_api_key == "":
        api_key = DEFAULT_API_KEY
    else:
        api_key = user_api_key

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            description = data["weather"][0]["description"]

            result_label.config(
                text=f"Temperature: {temp} °C\nHumidity: {humidity}%\nWind Speed: {wind} m/s\nWeather: {description}"
            )
        else:
            result_label.config(text="Invalid city or API key")

    except:
        result_label.config(text="Error connecting to API")

# Window
window = tk.Tk()
window.title("Weather App")
window.geometry("400x350")

title = tk.Label(window, text="Weather App", font=("Arial", 18))
title.pack(pady=10)

# API key input (optional)
api_label = tk.Label(window, text="API Key (Optional)")
api_label.pack()

api_entry = tk.Entry(window, width=40)
api_entry.pack(pady=5)

# City input
city_label = tk.Label(window, text="Enter City Name")
city_label.pack()

city_entry = tk.Entry(window, width=40)
city_entry.pack(pady=5)

# Button
search_button = tk.Button(window, text="Get Weather", command=get_weather)
search_button.pack(pady=15)

# Result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

window.mainloop()