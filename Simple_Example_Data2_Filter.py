#!flask/bin/python
from flask import Flask, jsonify, abort

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
        'title': u'Thomas',
        'lastname': u'Williams', 
        'inpatient': False
    }
]

@app.route('/', methods=['GET'])
def welcome():
    return "Server AHI 1.0"


@app.route('/ahi/api/v1.0/patients', methods=['GET'])
def get_tasks():
    return jsonify({'patients': patients})


@app.route('/ahi/api/v1.0/patients/<int:patient_id>', methods=['GET'])
def get_task(patient_id):
    patient = [patient for patient in patients if patient['patient_id'] == patient_id]
    if len(patient) == 0:
        abort(404)
    return jsonify({'patient': patient[0]})


if __name__ == '__main__':
    app.run(debug=True)