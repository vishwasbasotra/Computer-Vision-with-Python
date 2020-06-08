# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:35:08 2020

@author: Vishwas Basotra
"""
# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# importing openCV
import cv2

# creating variable to store image using openCV
img = cv2.imread('../DATA/00-puppy.jpg')

print(img)
print(type(img))
print(img.shape)

# displaying image
plt.imshow(img)

# matplotlib --> RED GREEN BLUE
# openCV --> BLUE GREEN RED
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)

# reading image in grayscale
img_gray = cv2.imread('../DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)

# displaying gray scale imgae passing, cmap='gray'
plt.imshow(img_gray, cmap='gray')

# resizing images
new_img = cv2.resize(fix_img,(1000,400))
plt.imshow(new_img)

# resizing by ratio
w_ratio = 0.5 # 50% of original height
h_ratio = 0.5 # 50% of original height
new_img = cv2.resize(fix_img,(0,0),fix_img,w_ratio,h_ratio)
plt.imshow(new_img)

# flipping image
new_img = cv2.flip(fix_img,0)
plt.imshow(new_img)

new_img = cv2.flip(fix_img,1)
plt.imshow(new_img)

# save image file
type(fix_img)
cv2.imwrite('fix_img.jpg',fix_img)

# displaying enlarge image 
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.imshow(fix_img)