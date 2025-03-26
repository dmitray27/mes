from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    messages.append(f"{data['sender']}: {data['message']}")
    return jsonify({"status": "OK"})

@app.route('/get_messages')
def get_messages():
    return jsonify({"messages": messages})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
