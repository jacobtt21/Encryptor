from flask import Flask, render_template, request
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

key = os.getenv('KEY_VALUE')
key.encode()
fernet = Fernet(key)

@app.errorhandler(500)
def our_bad(e):
    return render_template('index.html', message="Something is wrong, slack Jacob if something is wrong"), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enc/', defaults={'enc': None})
@app.route('/enc/<enc>')
def find(enc):
    encs = request.args.get('enc')
    encs.encode()
    return render_template('index.html', message = fernet.decrypt(encs.encode()).decode())