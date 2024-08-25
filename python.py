from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        data = request.json
        
        # Extracting values from JSON request
        user_id = data.get('user_id', '')
        college_email_id = data.get('college_email_id', '')
        college_roll_number = data.get('college_roll_number', '')
        numbers = data.get('numbers', [])
        alphabets = data.get('alphabets', [])
        
        # Process the alphabets to find the highest lowercase letter
        highest_lowercase = []
        if alphabets:
            # Filter out lowercase letters and find the maximum
            lowercase_letters = [ch for ch in alphabets if ch.islower()]
            if lowercase_letters:
                max_lowercase = max(lowercase_letters)
                highest_lowercase = [ch for ch in lowercase_letters if ch == max_lowercase]
        
        response = {
            'Status': 'Success',
            'User ID': user_id,
            'College Email ID': college_email_id,
            'College Roll Number': college_roll_number,
            'Array for numbers': numbers,
            'Array for alphabets': alphabets,
            'Array with the highest lowercase alphabet': highest_lowercase
        }
        
        return jsonify(response)
    
    elif request.method == 'GET':
        response = {
            'operation_code': '12345' 
        }
        
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
