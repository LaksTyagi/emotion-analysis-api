# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    fake_emotions = ["Happy", "Sad", "Anxious", "Excited", "Angry"]
    response = {
        "emotion": random.choice(fake_emotions),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
