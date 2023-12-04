import requests
import json
from datetime import datetime

# Constants
TARGET = "bing.com"
API_URL = "https://atlas.ripe.net/api/v2/measurements/"
API_KEY = "{Redacted For Security}"
NUM_PACKETS = 1
AF = 4
startTime = int(datetime.utcnow().timestamp()  - 14300) #100 seconds in the future, 14400 accounts for Utc -4
stopTime = int(datetime.utcnow().timestamp() + 72999) #24 hours and 899 seconds seconds after the startTime 
#startTime = int(datetime.utcnow().timestamp()  - 14300) #100 seconds in the future, 14400 accounts for Utc -4
#stopTime = int(datetime.utcnow().timestamp() - 13200) #930 Seconds after the startTime 

def startMeasurement(probe_ids):
    # Create the headers
    headers = {
        "Authorization": f"Key {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    probe_ids_str = ",".join(map(str, probe_ids))

    # Create the payload
    payload = {
        "definitions": [
            {
                "target": TARGET,
                "description": "24 Hour Project Starlink Test",
                "type": "ping",
                "af": AF,
                "packets": NUM_PACKETS,
                "interval": 900 
            }
        ],
        "probes": [
            {
                "requested": len(probe_ids), 
                "type": "probes",
                "value": probe_ids_str
            }
        ],
        "start_time": startTime,
        "stop_time": stopTime,
    }

    # Issue request
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 201:
        # Status Code 201 Indicates Successful HTTP Post
        data = response.json()
        print(data)
    else:
        # Request Failed
        print("Request has failed")
        print(response.content)
        print(response.status_code)


def getResults(measurement_id):
    api = f"https://atlas.ripe.net/api/v2/measurements/{measurement_id}/results/"
    #probe_ids = [62553]
    # payload = {
    #     "probe_ids": ",".join(map(str, probe_ids)),

    # }

    response = requests.get(api)

    if response.status_code == 200:
        # The request was successful
        data = response.json()
        results = data  # ['results']
        with open("traceroute.json", "w") as outfile:
            json.dump(data, outfile)
        print(results)
    else:
        # Request Failed
        print("Request has failed")
        print(response.status_code)

def startTraceroute(probe_ids):
    # Create the headers
    headers = {
        "Authorization": f"Key {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    probe_ids_str = ",".join(map(str, probe_ids))

    # Create the payload
    payload = {
        "definitions": [
            {
                "target": TARGET,
                "description": "Project Starlink Traceroute",
                "type": "traceroute",
                "af": AF,
                "packets": NUM_PACKETS,
            }
        ],
        "probes": [
            {
                "requested": len(probe_ids), 
                "type": "probes",
                "value": probe_ids_str
            }
        ],
        "is_oneoff": True
    }

    # Issue request
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 201:
        # Status Code 201 Indicates Successful HTTP Post
        data = response.json()
        print(data)
    else:
        # Request Failed
        print("Request has failed")
        print(response.content)
        print(response.status_code)

# startMeasurement or getResults function calls here
#startMeasurement([1005627, 24742, 26696, 1005561, 61366, 53798, 35751, 61537, 26834, 52955, 55492, 62868, 60323, 1005623, 17979, 19983, 61081, 54330, 62613, 62365, 62498, 1004978, 1004876, 20544, 61113,])
#getResults(52764390)
#startTraceroute([1005627, 24742, 26696, 1005561, 61366, 53798, 35751, 61537, 26834, 52955, 55492, 62868, 60323, 1005623, 17979, 19983, 61081, 54330, 62613, 62365, 62498, 1004978, 1004876, 20544, 61113,])
getResults(53099863)