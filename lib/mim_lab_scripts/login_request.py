# This contains the request script for attempting login.
import requests
from requests import ConnectionError

headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Cookie': 'PHPSESSID=lm7ogennlv8uh3j7dfp9e7iob3; security=impossible'}

setup_payload = {'create_db': 'Create+%2F+Reset+Database', 'user_token': '6cca1b3003163a13d7a968b2a9339391'}

s = requests.session()

# Initialize db if not done
while True:
    try:
        r = s.post('http://172.17.0.3/setup.php', headers=headers, params=setup_payload)
    except ConnectionError:
        pass

    try:
        r = s.post('http://172.17.0.2/setup.php', headers=headers, params=setup_payload)
    except ConnectionError:
        pass

    payload = {'username': 'admin', 'password': 'password', 'Login': 'Login',
               'user_token': '9130a5289116c09fd92f81030bb55f11'}

    # IP of dvwa container
    try:
        r = s.post('http://172.17.0.3/login.php', headers=headers, params=payload)
        print r.status_code
        print r.text
    except ConnectionError:
        pass
    try:
        r = s.post('http://172.17.0.2/login.php', headers=headers, params=payload)
        print r.status_code
        print r.text
    except ConnectionError:
        pass
