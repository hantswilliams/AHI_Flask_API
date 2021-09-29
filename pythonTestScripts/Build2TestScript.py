import requests 


testUrl = "http://localhost:5000/patients"


apiRequest = requests.get(testUrl)

print(apiRequest.text)

