import requests

api_url = "https://atlas.ripe.net/api/v2/probes/"
payload = {
    "asn_v4": 14593
}

starlink_probes = []

response = requests.get(api_url, params=payload)
if response.status_code == 200:
    # The request was successful
    data = response.json()
    results = data['results']
    starlink_probes.extend(results)
else:
    # Request Failed
    print("Request has failed")
    print(response.status_code)
connected = 0
for probe in starlink_probes:
    if(probe["status"]["name"] == 'Connected'):
        connected += 1
        print(probe["id"], probe["country_code"], probe["description"])
print(f"There are {connected} starlink probes connected")
