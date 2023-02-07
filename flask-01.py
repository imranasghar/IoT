## A simple flask Webserver programe
# Run the flask webserver

from flask import Flask
app = Flask(__name__)

# Route the root directory /
@app.route('/')

#Function helleo 

def hello():
    return 'Hello, USN IOT Class'

if __name__ == '__main__':
