#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:47:44 2022

@author: latchy
"""

#Generate two random numbers 
#Buy one number with the other 
#The change from the purchase needs to be printed 
#if no change than print a error message


import random

allMyMoneys = random.randint(0,999999)

while (1):
    costOfItemToPurchase = random.randint(0,9999)
    print("BANK ACCOUNT: ", allMyMoneys)
    print("ITEM COST: ", costOfItemToPurchase)
    attemptToBuy = allMyMoneys - costOfItemToPurchase
    if (attemptToBuy > 0):
        allMyMoneys = allMyMoneys - costOfItemToPurchase
        print("Item purchased: Money left ->", attemptToBuy)
    if (attemptToBuy < 0):
        print("Not enough moneys for the purchase (still need", attemptToBuy, "to complete purchase")
        break
    
    
