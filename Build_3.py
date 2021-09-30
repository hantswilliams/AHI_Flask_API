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
    return "Server AHI 1.0"


@app.route('/ahi/api/v1.0/patients', methods=['GET'])
def get_tasks():
    return jsonify({'patients': patients})





@app.route('/ahi/api/v1.0/patients/<var1>', methods=['GET'])
def get_patient_name(var1):
    patient = [x for x in patients if x['lastname'] == var1]
    if len(patient) == 0:
        return('Sorry nothing found! This search is case sensitive')
    return jsonify({'patient': patient[0]})



@app.route('/ahi/api/v1.0/patients/<int:patient_id>', methods=['GET'])
def get_patient_id(patient_id):
    patient = [i for i in patients if i['patient_id'] == patient_id]
    if len(patient) == 0:
        abort(404)
    return jsonify({'patient': patient[0]})


@app.route('/ahi/api/v1.0/patients/test/<int:patient_id>', methods=['GET'])
def get_patients_greaterthanID(patient_id):
    patient = [i for i in patients if i['patient_id'] < patient_id]
    if len(patient) == 0:
        abort(404)
    return jsonify({'patient': patient})


if __name__ == '__main__':
    app.run(debug=True)