import requests
import time

READ_API_KEY = "YOUR_READ_API_KEY"
CHANNEL_ID = "YOUR_CHANNEL_ID"
FIELD = 1  # field1 for temperature

url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{FIELD}.json?api_key={READ_API_KEY}&results=1"

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        feeds = data['feeds']
        if feeds:
            latest = feeds[0]
            print("Latest Temperature:", latest['field1'])
    else:
        print("Failed to retrieve data.")

    time.sleep(10)
