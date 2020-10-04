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
    }
]

@app.route('/', methods=['GET'])
def welcome():
    return "Server AHI 1.0"


@app.route('/ahi/api/v1.0/patients', methods=['GET'])
def get_tasks():
    return jsonify({'patients': patients})


@app.route('/ahi/api/v1.0/patients/<firstname>', methods=['GET'])
def get_patient_name(firstname):
    patient = [x for x in patients if x['firstname'] == firstname]
    if len(patient) == 0:
        abort(404)
    return jsonify({'patient': patient[0]})


@app.route('/ahi/api/v1.0/patients/<int:patient_id>', methods=['GET'])
def get_patient_id(patient_id):
    patient = [i for i in patients if i['patient_id'] == patient_id]
    if len(patient) == 0:
        abort(404)
    return jsonify({'patient': patient[0]})


if __name__ == '__main__':
    app.run(debug=True)