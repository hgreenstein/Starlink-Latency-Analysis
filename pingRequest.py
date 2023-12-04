import requests

api = "https://atlas.ripe.net/api/v2/measurements/"
payload = {
    "type": "ping", 
    "id": "1002"
}

response = requests.get(api, params=payload)

if response.status_code == 200:
    # The request was successful
    data = response.json()
    results = data['results'][0] 
    print("The ping time for probe id 1002 is " + str(results['stop_time'] - results['start_time']))
    print(data)
else:
    #Request Failed 
    print("Request has failed")
    print(response.status_code)
