from flask import Flask, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the API
@app.route('/hello', methods=['GET'])
def hello_world():
    # Return a simple JSON response
    return jsonify(message="Hello, World!")

# Run the app when the script is executed
if __name__ == '__main__':
    app.run(debug=True)


