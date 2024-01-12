from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import Counter

app = Flask(__name__)
CORS(app)

request_history = []

@app.route('/api/numbers', methods=['POST'])
def generate_numbers():
    try:
        int1 = int(request.form['int1'])
        int2 = int(request.form['int2'])
        limit = int(request.form['limit'])
        str1 = request.form['str1']
        str2 = request.form['str2']

        record_request('generate_numbers', int1=int1, int2=int2, limit=limit, str1=str1, str2=str2)
        
        if not isinstance(str1, str) or not str1.strip():
            raise ValueError("Invalid input. Please provide a valid string value for str1.")

        if not isinstance(str2, str) or not str2.strip():
            raise ValueError("Invalid input. Please provide a valid string value for str2.")

        numbers = []
        for i in range(1, limit+1):
            if (i % int1 == 0) and (i % int2 == 0):
                numbers.append(f"{str1}{str2}")
            elif i % int1 == 0:
                numbers.append(str1)
            elif i % int2 == 0:
                numbers.append(str2)
            else:
                numbers.append(f"{i}")
        ans = ','.join(numbers)
        return jsonify(ans)
        
    except ValueError as e:
        return jsonify({'error': 'Invalid input. Please provide valid integer values for int1, int2, and limit.'}), 400

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    if not request_history:
        return jsonify({'error': 'No statistics available'}), 404
    
    most_used_request = max(request_history, key=request_history.count, default=None)
    most_used_hits = request_history.count(most_used_request)
    
    most_recent_request = request_history[-1]
    most_recent_hits = request_history.count(most_recent_request)

    response_str = f"Most used request: {most_used_request[1]} with {most_used_hits} Hits,\n\nMost recent request: {most_recent_request[1]} with {most_recent_hits} Hits"
    return response_str, 200

def record_request(endpoint, **params):
    request_history.append((endpoint, params))

if __name__ == '__main__':
    app.run(debug=True)