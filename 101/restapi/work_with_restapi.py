# pip install requests
import requests

response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code) #404

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code) #200

print(response.json())

#{'message': 'success', 'people': [{'name': 'Alexey Ovchinin', 'craft': 'ISS'}, {'name': 'Nick Hague', 'craft': 'ISS'}, {'name': 'Christina Koch', 'craft': 'ISS'}, {'name': 'Alexander Skvortsov', 'craft': 'ISS'}, {'name': 'Luca Parmitano', 'craft': 'ISS'}, {'name': 'Andrew Morgan', 'craft': 'ISS'}], 'number': 6}


# Work with Json
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

# {
#     "message": "success",
#     "number": 6,
#     "people": [
#         {
#             "craft": "ISS",
#             "name": "Christina Koch"
#         },
#         {
#             "craft": "ISS",
#             "name": "Alexander Skvortsov"
#         },
#         {
#             "craft": "ISS",
#             "name": "Luca Parmitano"
#         },
#         {
#             "craft": "ISS",
#             "name": "Andrew Morgan"
#         },
#         {
#             "craft": "ISS",
#             "name": "Oleg Skripochka"
#         },
#         {
#             "craft": "ISS",
#             "name": "Jessica Meir"
#         }
#     ]
# }

# Passing parameters to api

parameters = {
    "lat": 40.71,
    "lon": -74
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response.json())

# {
#     "message": "success",
#     "request": {
#         "altitude": 100,
#         "datetime": 1576288308,
#         "latitude": 40.71,
#         "longitude": -74.0,
#         "passes": 5
#     },
#     "response": [
#         {
#             "duration": 218,
#             "risetime": 1576326149
#         },
#         {
#             "duration": 625,
#             "risetime": 1576331698
#         },
#         {
#             "duration": 629,
#             "risetime": 1576337500
#         },
#         {
#             "duration": 562,
#             "risetime": 1576343385
#         },
#         {
#             "duration": 580,
#             "risetime": 1576349242
#         }
#     ]
# }

# this works as well
requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74").json()

# select a specific part of the json
requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74").json()['requests']

# same things but formatted
pass_times = response.json()['response']
jprint(pass_times)

# extract specific values and add to dictionnary
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

# convert the file time format to date time

from datetime import datetime

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)


# 2019-09-09 21:27:59
# 2019-09-09 23:01:58
# 2019-09-10 00:39:04
# 2019-09-10 02:17:11
# 2019-09-10 03:54:34