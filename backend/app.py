from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'index.html')


@app.route('/script.js')
def serve_script():
    return send_from_directory('../frontend', 'script.js')

# For testing
@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.get_json()
    print("Received:", data)
    return jsonify({"message": "Data received!", "you_sent": data})


@app.route('/style.css')
def serve_style():
    return send_from_directory('../frontend', 'style.css')


if __name__ == '__main__':
    app.run(debug=True)
