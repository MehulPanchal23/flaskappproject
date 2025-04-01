from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Mehul, welcome to DevOps Zero To Hero (Junoon  Batch 9), Happy Learning Guys'

@app.route('/health')
def health():
    return 'Server is up and running'
