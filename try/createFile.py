#!/usr/bin/env python3

file = open("sample_file.txt",'a+')
file.writelines(["\nIt does not matter if exists or not!", "\nI will write on it."])
file.close()