#!/usr/bin/env python3
import os
file = open("new_file.txt", 'a+')
file.write("Hello World\n")
file.write("galileo galilei\n".capitalize())
file.write("JOHANES KEPLER\n".lower())
file.write("edwin hubble\n".upper())
file.write("NiCoLaS CoPeRnIcO\n".title())
file.write("eDMOND hALLEY\n".swapcase())
file_size = os.stat("new_file.txt")
print("Size of file :", file_size.st_size, "bytes It's in memory.")
file.close()
file_size = os.stat("new_file.txt")
print("Size of file :", file_size.st_size, "bytes. It's on disk")