from flask import Flask, request

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def post_endpoint():
    data = request.get_json()  # Get the JSON data from the request
    if 'text' in data:
        received_text = data['text']
        print("Received text:", received_text)
        return "Text received successfully!"
    else:
        return "Invalid JSON payload."

if __name__ == '__main__':
    app.run()
