from flask import Flask, request, jsonify
from interpretor import DreamInterpretor

app = Flask(__name__)

@app.route('/interpret_dream', methods=['POST'])
def interpret_dream():
    data = request.get_json()
    user_input = data['user_input']  # Assuming the user input is provided in the 'user_input' field

    # Call your chatbot function
    response = DreamInterpretor(user_input)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)