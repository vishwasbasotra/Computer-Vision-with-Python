# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 00:29:27 2020

@author: Vishwas Basotra
"""
# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

# creating blank image
blank_img = np.zeros((512,512,3), dtype=np.int32)
print(blank_img.shape)
plt.imshow(blank_img)

# Shapes
## Rectangle
cv2.rectangle(img=blank_img,
              pt1=(400,10),
              pt2=(500,100),
              color=(0,0,255),
              thickness=6
              ) 
plt.imshow(blank_img)

cv2.rectangle(img=blank_img,
              pt1=(200,200),
              pt2=(300,300),
              color=(255,0,0),
              thickness=8
              )
plt.imshow(blank_img)

## Circle
cv2.circle(img=blank_img,
           center=(100,100),
           radius=60,
           color=(0,255,0),
           thickness=4
           )
plt.imshow(blank_img) 

## Filled in 
cv2.circle(img=blank_img,
           center=(400,400),
           radius=60,
           color=(0,255,0),
           thickness=-1
           )
plt.imshow(blank_img) 

## Line
cv2.line(img=blank_img,
         pt1=(0,0),
         pt2=(512,512),
         color=(0,0,255),
         thickness=10
         )
plt.imshow(blank_img)

## Text 
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img=blank_img,
            text='HELLO!',
            org=(100,500),
            fontFace=font,
            fontScale=2,
            color=(255,0,0),
            thickness=4
            )
plt.imshow(blank_img)

## Polygons
blank_img = np.zeros((512,512,3), dtype=np.int32)
vertices = np.array([ [100,300],[200,200],[400,300],[200,400] ],dtype=np.int32)
pts = vertices.reshape(-1,1,2)
cv2.polylines(blank_img,
              [pts],
              isClosed=True,
              color=(255,0,0),
              thickness=3
              )
plt.imshow(blank_img)