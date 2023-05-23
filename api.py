from flask import Flask, request
from restPrivateGPT import get_answer

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def post_endpoint():
    data = request.get_json()  # Get the JSON data from the request
    if 'text' in data:
        answer = get_answer(data['text'])
        return answer
    else:
        return "Invalid JSON payload."

if __name__ == '__main__':
    app.run()
