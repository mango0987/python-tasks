import requests
import matplotlib.pyplot as plt
import datetime

# -------------------------------
# Step 1: Setup API details
# -------------------------------
API_KEY = "e7cbdf8f2b55cdf388a98b2b6c092cd2"  # Get from https://openweathermap.org/api
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# -------------------------------
# Step 2: Fetch data from API
# -------------------------------
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
else:
    print("Error fetching data:", response.status_code)
    exit()

# -------------------------------
# Step 3: Extract required info
# -------------------------------
dates = []
temps = []

for forecast in data["list"]:
    dt_txt = forecast["dt_txt"]
    temp = forecast["main"]["temp"]

    dates.append(datetime.datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S"))
    temps.append(temp)

# -------------------------------
# Step 4: Data Visualization
# -------------------------------
plt.figure(figsize=(10, 5))
plt.plot(dates, temps, marker="o", linestyle="-", color="b", label="Temperature (°C)")

plt.title(f"5-Day Weather Forecast for {CITY}", fontsize=14)
plt.xlabel("Date & Time", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

# Save the dashboard as an image
plt.savefig("weather_dashboard.png")
plt.show()
