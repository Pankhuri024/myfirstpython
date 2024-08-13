from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World Pankhuri'

if __name__ == '__main__':
    # Specify the port here (e.g., 8080) and the host (default is 127.0.0.1)
    app.run(host='0.0.0.0', port=8080, debug=True)
