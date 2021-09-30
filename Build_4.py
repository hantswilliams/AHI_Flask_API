#!flask/bin/python
from flask import Flask, jsonify, abort, request

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
    return "Server AHI 2.0"


@app.route('/ahi/api/v1.0/patients', methods=['GET'])
def get_tasks():
    return jsonify({'patients': patients})


@app.route('/ahi/api/v1.0/patients/<firstname_entered>', methods=['GET'])
def get_patient_name(firstname_entered):
    patient = [x for x in patients if x['firstname'] == firstname_entered]
    if len(patient) == 0:
        return('Sorry nothing found! This search is case sensitive')
    return jsonify({'patient': patient[0]})


@app.route('/ahi/api/v1.0/patients/<int:patient_id>', methods=['GET'])
def get_patient_id(patient_id):
    patient = [i for i in patients if i['patient_id'] == patient_id]
    if len(patient) == 0:
        abort(404)
    return jsonify({'patient': patient[0]})




#Create a new patient
@app.route('/ahi/api/v1.0/add_patient', methods=['POST'])
def create_task():
    
    if not request.json or not 'patient_id' in request.json:
        abort(400)

    patient = {
        'patient_id': request.json['patient_id'],
        'firstname': request.json.get('firstname', ""),
        'lastname': request.json.get('lastname', ""),
        'inpatient': request.json.get('inpatient', "")
    }
    
    patients.append(patient)
    
    return jsonify({'patient succesfully added': patient}), 201










if __name__ == '__main__':
    app.run(debug=True)