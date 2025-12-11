from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

KEYS = [
    "WC7X3-12347",
    "WC7X3-89562",
    "WC7X3-45679",
    "WC7X3-23450",
    "WC7X3-67893",
    "WC7X3-01122",
    "WC7X3-88991",
    "WC7X3-34561",
    "WC7X3-90124",
    "WC7X3-56788"
]

@app.route('/')
def home():
    return "License Key API - Running"

@app.route('/get-key')
def get_key():
    key = random.choice(KEYS)
    return jsonify({"key": key})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
