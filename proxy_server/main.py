from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from OpenSSL import crypto

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# cert_file = '/path/to/your/certificate'
# cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
# subject = cert.get_subject()
# issued_to = subject.CN    # the Common Name field
# issuer = cert.get_issuer()
# issued_by = issuer.CN


@app.route('/certs', methods=['POST'])
@cross_origin()
def hello_world():
    try:    
        cert_file = request.files['file']
        contents = cert_file.read()
        cert  = crypto.load_certificate(crypto.FILETYPE_PEM, contents)
        pub_key = cert.get_pubkey()
        pub_key_string = crypto.dump_publickey(crypto.FILETYPE_PEM, pub_key)
        cert_values = {
            'CN' : cert.get_subject().CN,
            'O': cert.get_subject().O,
            'emailAddress': cert.get_subject().emailAddress,
            'L': cert.get_subject().L,
            'hash': pub_key_string
        }
        return cert_values
    except Exception as E:
        print(E)

    return {}


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)