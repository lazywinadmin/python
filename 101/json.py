import json
with open("secrets.json") as json_data_file:
    data = json.load(json_data_file)
print(data)
print(data['appId'])