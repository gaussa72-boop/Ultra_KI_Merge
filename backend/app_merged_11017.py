from flask import Flask, send_from_directory, jsonify, request
from backend.quantum_mirror_backend import QuantumMirrorBackend
import os

app = Flask(__name__, static_folder='web', template_folder='web')
backend = QuantumMirrorBackend()

@app.route('/')
def index():
    return send_from_directory('web', 'index.html')

@app.route('/health')
def health():
    return jsonify({'status':'healthy','service':'Quantum Mirror Wonderland'})

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return jsonify({'error':'missing username/email'}),400
    res=backend.register_user(username,email)
    return jsonify(res),201

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('web/static', path)

if __name__=='__main__':
    port=int(os.getenv('PORT',5000))
    app.run(host='0.0.0.0', port=port, debug=True)

