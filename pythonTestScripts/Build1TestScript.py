import requests 


testUrl = "http://localhost:5000/"


apiRequest = requests.get(testUrl)

print(apiRequest.text)

