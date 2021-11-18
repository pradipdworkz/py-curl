import pycurl
import json
from io import BytesIO
import os
from flask import Flask, make_response
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

url = os.getenv('API_URL')
certificate = os.path.abspath('./certificate.pem')
key =  os.path.abspath('./key.pem')
passphrase = "1234"
header = ['Accept: application/json']

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/curl')
def get_profiles():
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.SSLCERT, certificate)
    c.setopt(pycurl.SSLKEY, key)
    c.setopt(pycurl.SSLCERTPASSWD, passphrase)
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.SSL_VERIFYPEER, 0);
    c.setopt(pycurl.SSL_VERIFYHOST, 0);
    c.setopt(pycurl.HTTPHEADER, header)

    c.setopt(c.WRITEDATA, buffer)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.perform()
    data = json.loads(buffer.getvalue())
    c.close()
    return make_response({'status': 'success', 'data': data})