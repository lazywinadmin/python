# pip install requests
import requests

#response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
#print(response.status_code) #404

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code) #200

print(response.json())
#{'people': [{'craft': 'ISS', 'name': 'Andrew Morgan'}, {'craft': 'ISS', 'name': 'Oleg Skripochka'}, {'craft': 'ISS', 'name': 'Jessica Meir'}], 'message': 'success', 'number': 3}




