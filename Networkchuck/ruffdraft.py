#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:33:12 2022

@author: latchy
"""

print("Hello!, \n\n Welcome to Lord Latchy's coffee shop")

name = input(("\n\n What is your name?! :>"))

if name == "Ben" or name == "Patrica":
   evil_status = input("Are you evil? \n")
if evil_status == "Yes":
    print(" You're not welcome here " + name + ", get out of here")
    exit()
else:
    print("Hello " + name + ", thank you for coming in \n\n\n")
    
    
    
    
