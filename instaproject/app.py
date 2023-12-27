#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:49:36 2022

@author: latchy
"""

import cv2
import numpy as np

#Dummy function that does nothing 
def dummy(value):
    pass

#Define convolution kernels
identity_kernel = np.array([[0,0,0], [0,1,0], [0,0,0]])
sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
guassian_kernel1 = cv2.getGaussianKernel(3, 0)
guassian_kernel2 = cv2.getGaussianKernel(5, 0)
box_kernel = np.array([[1,1,1], [1,1,1], [1,1,1]], np.float32) / 9.0
#1+2=3+4+5) / 5 = 1 * 1/5 + 2 * 1/5 + 3 * 1/5 + 4 * 1/5 + 5 *1/5

kernels = [identity_kernel, sharpen_kernel, guassian_kernel1, guassian_kernel2, box_kernel]

#Read in an image, make a gray scale copy
color_original = cv2.imread('test.jpg')
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)


#Creating the main UI (Window and track bars)

cv2.namedWindow('app')
#Arguments: TrackBar, Windowname, value (inital value), count(Max Value), on change(Event handler)
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)

#name=brightness, inital value=50, max value=100, event handler=dummy
cv2.createTrackbar('brightness', 'app', 100, 200, dummy)

#TODO: Update max value to number of filters
cv2.createTrackbar('filter', 'app', 0, len(kernels)-1, dummy)

cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

#Main UI Loop
count = 1
while True:
    #TODO: Read all trackbar values
    grayscale = cv2.getTrackbarPos('grayscale', 'app')
    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brigtness', 'app')
    kernel_idx = cv2.getTrackbarPos('filter', 'app')
    
    #TODO: Apply the filters
    color_modified = cv2.filter2D(color_original, -1, kernels[kernel_idx])
    gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel_idx])
    
    #TODO: Apply the brightness and contract
    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros_like(color_original), 0, brightness -50)
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros_like(gray_original),0, brightness -50)
    
    #TODO: Wait for wait key (100 Miliseconds)
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    
    elif key == ord('s'):
        # Save image
        if grayscale == 0:
            cv2.imwrite('output-{}.png'.format(count), color_modified)
        else:
            cv2.imwrite('output-{}.png'.format(count), gray_modified)
        count += 1
    
    
    
    #Show the image
    if grayscale == 0:
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)

#Window clean up
cv2.destroyALLWINDOWS()
