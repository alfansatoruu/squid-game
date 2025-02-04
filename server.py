from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  

@app.route('/run-python', methods=['POST'])
def run_python():
    try: 
        result = subprocess.run(
            ['python', 'script.py'],
            capture_output=True,
            text=True,
            check=True
        )
        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        })
    except subprocess.CalledProcessError as e:
        return jsonify({
            'success': False,
            'output': e.stdout,
            'error': e.stderr
        }), 500

if __name__ == '__main__':
    app.run(debug=True)