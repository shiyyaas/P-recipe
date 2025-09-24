from flask import Flask #flask for server
from pymongo import MongoClient

backendd = Flask(__name__)

@backendd.route('/')
def home():
    return "Hello from my virtual environment!"

if __name__ == '__main__':
    backendd.run(debug=True)