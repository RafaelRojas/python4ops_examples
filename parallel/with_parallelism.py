#!/usr/bin/env python3
import os
import multiprocessing
import concurrent.futures
import time
from PIL import Image, ImageFilter


imagelist = [i for i in os.listdir('.') if i.endswith('jpg')]
start = time.perf_counter()
size = (1200, 1200)

def augment_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'augmented-{img_name}')
    print(f'{img_name} was augmented...')

if __name__ == "__main__":
	with concurrent.futures.ProcessPoolExecutor() as executor:
	  	executor.map(augment_image, imagelist)
	end = time.perf_counter()
	print(f'Finished in {round(end-start, 2)} seconds') 

