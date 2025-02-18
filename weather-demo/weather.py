import tkinter as tk
import requests

# Function to fetch weather
def get_weather():
    city = city_entry.get()  # Get city from input
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            result_label.config(text=f"Temperature: {temp}°C\nCondition: {desc.capitalize()}")
        else:
            result_label.config(text="City not found.")
    except Exception as e:
        result_label.config(text="Error fetching data.")

# Create GUI window
app = tk.Tk()
app.title("Weather App")
app.geometry("300x200")

# Input field
city_label = tk.Label(app, text="Enter City:")
city_label.pack(pady=5)

city_entry = tk.Entry(app, width=25)
city_entry.pack(pady=5)

# Button
fetch_button = tk.Button(app, text="Get Weather", command=get_weather)
fetch_button.pack(pady=10)

# Result display
result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the app
app.mainloop()
