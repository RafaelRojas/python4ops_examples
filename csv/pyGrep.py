#!/usr/bin/env python3
#search a pattern using regex.

import re

patrn = "Mexico"
file_one = open("salesRecords.csv", "r")
instances = 0

for word in file_one:
    if re.search(patrn, word):
        instances+=1
print(instances)