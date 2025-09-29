from flask import Flask
from flask_cors import CORS  
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # this allows the communications btw frontend and backend

@app.route('/')
def hello():
    return "Hello World! Flask is working! 🎉"

if __name__ == '__main__':
    app.run(debug=True, port=5000)