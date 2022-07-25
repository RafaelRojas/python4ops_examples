#!/usr/bin/env python3

import requests
from requests.exceptions import HTTPError
import json
import urllib3
urllib3.disable_warnings()

request_url = "https://swapi.dev/api/films/"
try:
    request = requests.get(request_url, verify=False)
    print(request.status_code)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}') 
except Exception as err:
    print(f'Other error occurred: {err}') 
else:
    print('Success!')



#request = requests.get(request_url, verify=False)
#request_json = (json.loads(request.text))
