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

if __name__ == '__main__':
    app.run(debug=True)