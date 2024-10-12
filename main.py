from flask import Flask, jsonify, request
from flask_cors import CORS
from meta_ai_api import MetaAI

ai = MetaAI() 

app = Flask(__name__)
# CORS(app)  # Habilita CORS para todas las rutas

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_response/<user_text>', methods=['GET'])
def get_response(user_text):
    response = ai.prompt(message=user_text)
    answer = response['message']
    if response['sources']:
        answer += f"\n\nFuentes: {', '.join(response['sources'])}"
    print(answer)
    return jsonify(answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
