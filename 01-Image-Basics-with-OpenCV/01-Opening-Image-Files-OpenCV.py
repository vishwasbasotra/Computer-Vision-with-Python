# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 00:07:39 2020

@author: Vishwas Basotra
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('../DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy',img)
    # if we waited atleast 1 ms AND we've pressed Esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()