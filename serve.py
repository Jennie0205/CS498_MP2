from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        # Handling HTTP POST request
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return 'Stressing CPU process started.\n', 200
    elif request.method == 'GET':
        # Handling HTTP GET request
        private_ip = socket.gethostbyname(socket.gethostname())
        return jsonify({'private_ip': private_ip}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
