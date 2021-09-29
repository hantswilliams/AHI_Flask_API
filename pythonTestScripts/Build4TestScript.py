import requests 


testUrl = "http://localhost:5000/ahi/api/v1.0/add_patient"

patientTest = {
        'patient_id': '222222',
        'firstname': 'example2',
        'lastname': 'example3',
        'inpatient': True
    }

apiRequest = requests.post(testUrl, json=patientTest)

