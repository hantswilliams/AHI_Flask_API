#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

patients = [
    {
        'patient_id': 1,
        'firstname': u'Hants',
        'lastname': u'Williams', 
        'inpatient': True
    },
    {
        'patient_id': 2,
        'firstname': u'Thomas',
        'lastname': u'Williams', 
        'inpatient': False
    },
    {
        'patient_id': 3,
        'firstname': u'Kyle',
        'lastname': u'Jones',
        'inpatient': False
    },
        {
        'patient_id': 4,
        'firstname': u'Marie',
        'lastname': u'Guiteirrez',
        'inpatient': False
    },
        {
        'patient_id': 5,
        'firstname': u'Amanda',
        'lastname': u'Power',
        'inpatient': True
    },
        {
        'patient_id': 6,
        'firstname': u'Manleen',
        'lastname': u'Chhabra',
        'inpatient': True
    }
]


@app.route('/', methods=['GET'])
def welcome():
    return "Server AHI 0.01"



@app.route('/patients', methods=['GET'])
def patientsEMR():
    return jsonify(patients)

if __name__ == '__main__':
    app.run(debug=True)