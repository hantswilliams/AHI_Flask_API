from flask import Flask

app = Flask(__name__)


## In order to run this, all you need to do is naviagate to the folder in which this 
## file lives, and then type the follow below and press enter: 
## python Build_1.py

## 222 this is the second change

@app.route('/', methods=['GET'])
def hello():
    return "Hello 😀😀😀😀😀😀! heeyyyyyyy"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


## This will start up a 'development' server on your own local machine 