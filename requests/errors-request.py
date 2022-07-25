#!/usr/bin/env python3

import requests
from requests.exceptions import HTTPError
import json
import urllib3
urllib3.disable_warnings()

request_url = "https://swapi.dev/api/films/"
request = requests.get(request_url, verify=False)

if request.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
