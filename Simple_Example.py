from flask import Flask
app = Flask(__name__)


## In order to run this, all you need to do is naviagate to the folder in which this 
## file lives, and then type the follow below and press enter: 
## python Simple_Example.py

## This is an example of pushing a change to Hants's GitHub Repository

@app.route('/')
def hello():
    return "Hello Hants!"

if __name__ == '__main__':
    app.run(debug=True)


## This will start up a 'development' server on your own local machine 