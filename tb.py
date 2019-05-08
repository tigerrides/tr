import hashlib
import random
from base64 import b64encode
from datetime import datetime
import requests
import json

url = 'https://tigerbook.herokuapp.com/api/aPNwzUMmFu2UtWVMtil8'
created = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
nonce = ''.join([random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=') for i in range(32)])
username = 'nbs'
password = '9194a9a482af7e5bc117c255a7a4d82a'
generated_digest = b64encode(hashlib.sha256(nonce.encode('utf-8') + created.encode('utf-8') + password.encode('utf-8')).digest()).decode()
headers = {
    'Authorization': 'WSSE profile="UsernameToken"',
    'X-WSSE': 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % (username, generated_digest, b64encode(nonce.encode()).decode(), created)
}

r = requests.get(url + '/' + 'nbs', headers=headers)
print(r.text)

