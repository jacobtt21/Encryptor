from flask import Flask, render_template, request
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

key = os.getenv('KEY_VALUE')
password = os.getenv('PASS_VALUE')
key.encode()
fernet = Fernet(key)

@app.errorhandler(500)
def our_bad(e):
    return render_template('index.html', message="Ensure that you are inputting the correct input!"), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enc/', defaults={'enc': None, 'passw': None})
@app.route('/enc/<enc>/<passw>')
def find(enc, passw):
    passes = request.args.get('passw')
    encs = request.args.get('enc')
    encs = encs.encode()
    if passes == password:
        return render_template('index.html', message = fernet.decrypt(encs).decode())
    else:
        return render_template('index.html', message = "incorrect password")

if __name__ == '__main__':
    app.run(debug=True)