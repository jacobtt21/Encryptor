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

@app.errorhandler(405)
def our_bad(e):
    return render_template('index.html'), 405

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enc', methods=['POST'])
def find():
    if request.method == 'POST':
        passes = request.form['passw']
        encs = request.form['enc']
        encs = encs.encode()
        if passes == password:
            return render_template('index.html', message = fernet.decrypt(encs).decode())
        else:
            return render_template('index.html', message = "incorrect password")

##Test Cases
##gAAAAABhVp4UJe0o1706MiFXuQnJxqIlWAPlv8j0qGZSi_CRiGZtNnPmmVNUwXG97TZ1yTTOwpauL3ZIPhSNIMWL0oqXvC3r5VsnGFMywrimKUkKZ8SHtrY=
##gAAAAABhVp4s2uzu2p_jh5V0HRLDrlnh2jRLcWTJWTTSB-YlZ984y9jGzwZeyFUOFIDmgy3nKjvUwLhTIk2E9EmN2qZOZupidxrO6s7Y-oeaFlBrqPvadJ4=

if __name__ == '__main__':
    app.run(debug=True)