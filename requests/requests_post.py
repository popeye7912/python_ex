import requests, json
URL = "https://google.com"

# data with json
data = {"outer": {"inner": "value"}}
response = requests.post(URL, data=data)
response = requests.post(URL, data=json.dumps(data))

# json
response = requests.post(URL, json={"name": "test"})

# files
files = {'file': open('report.xls', 'rb')}
r = requests.post(URL, files=files)