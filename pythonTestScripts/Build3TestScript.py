import requests 


testUrl1 = "http://localhost:5000/ahi/api/v1.0/patients/4"
testUrl2 = "http://localhost:5000/ahi/api/v1.0/patients/Hants"


apiRequest1 = requests.get(testUrl1)
apiRequest2 = requests.get(testUrl2)


print('ApiTest1: ', apiRequest1.text)
print('ApiTest2: ', apiRequest2.text)

