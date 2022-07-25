#!/usr/bin/env python3
import os
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

for f in imagelist:
    augment_image(f)
end = time.perf_counter()
print(f'Finished in {round(end-start, 2)} seconds') 