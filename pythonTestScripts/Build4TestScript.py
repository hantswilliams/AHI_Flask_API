import requests 


testUrl = "http://127.0.0.1:5000/ahi/api/v1.0/add_patient"

patientTest = {
        'patient_id': '340000',
        'firstname': 'example55',
        'lastname': 'example66',
        'inpatient': True
    }

apiRequest = requests.post(testUrl, json=patientTest)

apiRequest.status_code



testUrl = "http://127.0.0.1:5000/ahi/api/v1.0/patients"
apiRequest = requests.get(testUrl)
print(apiRequest.text)
