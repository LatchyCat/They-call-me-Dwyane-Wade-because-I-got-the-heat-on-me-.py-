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
#Creating the main UI (Window and track bars)

cv2.namedWindow('trackbars')
#Arguments: TrackBar, Windowname, value (inital value), count(Max Value), on change(Event handler)
cv2.createTrackbar('contrast', 'trackbars', 1, 100, dummy)

#name=brightness, inital value=50, max value=100, event handler=dummy
cv2.createTrackbar('brightness', 'trackbars', 50, 100, dummy)

#TODO: Remove this line!
cv2.waitKey(0)

#Window clean up
cv2.destroyALLWINDOWS()
