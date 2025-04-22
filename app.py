#!/usr/bin/env python3

from flask import Flask, Response

# Create Flask application instance
app = Flask(__name__)

# Define constants for server configuration
HOSTNAME = '127.0.0.1'
PORT = 3000

# Create a catch-all route that handles all HTTP requests
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    # Return 'Hello, World!\n' with text/plain content type and 200 status
    return Response('Hello, World!\n', mimetype='text/plain', status=200)

if __name__ == '__main__':
    # Log server URL upon startup
    print(f"Server running at http://{HOSTNAME}:{PORT}/")
    
    # Start the Flask server on 127.0.0.1:3000
    # host='127.0.0.1' ensures the server only listens on localhost
    # port=3000 overrides Flask's default port 5000
    app.run(host=HOSTNAME, port=PORT)