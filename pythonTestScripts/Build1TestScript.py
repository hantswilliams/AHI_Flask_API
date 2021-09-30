import requests 


testUrl = "http://127.0.0.1:5000/"


apiRequest = requests.get(testUrl)

print(apiRequest.text)

