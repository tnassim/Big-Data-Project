import json
import time
import urllib.request

from kafka import KafkaProducer

API_KEY = "2970bcb2d11440f4dcee753066f9d1f4e0ef6b0f" # FIXME Set your own API key here
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        producer.send("bike-stations", json.dumps(station).encode())
    print("{} Produced {} station records".format(time.time(), len(stations)))
    time.sleep(1)