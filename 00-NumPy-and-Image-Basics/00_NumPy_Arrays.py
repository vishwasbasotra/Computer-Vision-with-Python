# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:30:07 2020

@author: Vishwas Basotra
"""
import numpy as np
 
mylist = [1,2,3,4]
type(mylist)

myarray = np.array(mylist).reshape(2,2)
print(myarray)
print(type(myarray))

print(np.arange(0,9).reshape(3,3))
print(np.zeros((5,5)))

print(np.ones((3,3)))

np.random.seed(101)
arr = np.random.randint(0,100,10).reshape(5,2)
print(arr)
print(arr.max(),arr.argmax())
print(arr.min(),arr.argmin())

new_arr = arr.copy()
print(new_arr)