from flask import Flask, request, jsonify
from flask_cors import CORS

from controllers.Methods import Bisection
from controllers.Validation import BisectionVars  # You’ll likely need to adapt this

app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Approximation API. Where this is just wasteland"})

@app.route('/bisection', methods=['POST'])
def bisection():
    data = request.get_json()
    try:
        vars = BisectionVars(**data)  # If BisectionVars is a pydantic model, this will work
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    bisection_method = Bisection(vars)
    result = bisection_method.startIterations()
    return jsonify({"data": result})

@app.route('/tables', methods=['GET'])
def tables():
    return jsonify({"message": "Tables endpoint coming soon"})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
