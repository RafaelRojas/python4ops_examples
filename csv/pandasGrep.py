#!/usr/bin/env python3
#search a pattern using regex.

import re
import pandas as pd

patrn = "Mexico"
#file_one = open("salesRecords.csv", "r")
file_one = pd.read_csv("salesRecords.csv", engine="pyarrow")
instances = 0


for index, row in file_one.iterrows():
#    print(row[1])
    if row[1] == patrn:
        instances+=1
print(instances)
