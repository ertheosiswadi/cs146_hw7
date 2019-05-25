#!/usr/bin/python3
import sys
from PIL import Image
from numpy import array
from numpy.linalg import norm
from math import pow

bear = Image.open('pic.jpg')
pix_bear = bear.load()
print(bear.size)
print(pix_bear[0,0])

for i in range(200,bear.size[0]):
    for j in range(150,bear.size[1]):
        pix_bear[i,j] = (0,0,0)
bear.save('./newpic.jpg')