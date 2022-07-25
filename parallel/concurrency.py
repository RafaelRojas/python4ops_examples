#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
import urllib.request as ur

datas = []

def get_from(url):
    connection = ur.urlopen(url)
    data = connection.read()
    datas.append(data)

urls = [
    "https://python.org",
    "https://docs.python.org/"
    "https://wikipedia.org",
    "https://imdb.com",    
]

with ThreadPoolExecutor() as ex:
    for url in urls:
        ex.submit(get_from, url)
       
# let's just look at the beginning of each data stream
# as this could be a lot of data
print ([_[:200] for _ in datas])
