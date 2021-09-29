import requests 


testUrl = "http://localhost:5000/ahi/api/v1.0/patients"

apiRequest = requests.get(testUrl, auth=('ahi', '2021'))

print(apiRequest.text)

