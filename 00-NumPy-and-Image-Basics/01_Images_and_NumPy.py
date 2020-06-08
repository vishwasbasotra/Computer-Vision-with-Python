# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:48:48 2020

@author: Vishwas Basotra
"""

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

pic = Image.open('../DATA/00-puppy.jpg')

pic

print(type(pic))

pic_arr = np.array(pic)
print(type(pic_arr))
print(pic_arr.shape)

plt.imshow(pic_arr)

pic_red = pic_arr.copy()

# R G B
plt.imshow(pic_red[:,:,0], cmap='gray')
plt.imshow(pic_red[:,:,1], cmap='gray')
plt.imshow(pic_red[:,:,2], cmap='gray')

pic_red[:,:,1] = 0
plt.imshow(pic_red)

pic_red[:,:,2] = 0
plt.imshow(pic_red)

print(pic_red.shape)