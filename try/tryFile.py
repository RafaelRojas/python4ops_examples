#!/usr/bin/env python3

try:
    file = open("sample_file.txt", 'r')
    file.writelines(["\nFile exists!", "\nSee you soon!."])
    file.close()
except FileNotFoundError:
    file = open("sample_file.txt", 'w')
    file.writelines(["\nFile created!", "\nSee you soon!."])
    file.close()