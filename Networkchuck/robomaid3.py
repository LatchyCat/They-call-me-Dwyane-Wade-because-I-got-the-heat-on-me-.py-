#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 07:27:01 2022

@author: latchy
"""

# =============================================================================
# print("Hello Sir and welcome to coffee hut \n\n ")
# 
# name = input("What is your name\n\n ")
# 
# if name == "Ben":
#  print("\n you're not welcome here Evil Ben! \n")
#  
# else:
#     print("\n Hello " + name + " ,thank you so much for coming in today \n\n")
# =============================================================================
 
 

# =============================================================================
# if 2 > 3:
#     print("True")
#     print("Still True")
#     
# else:
#     print("False")
#     print("Still False")
# =============================================================================

# =============================================================================
# print("Hello Sir and welcome to coffee hut \n\n ")
# 
# name = input("What is your name \n\n ")
# 
# if name == "Ben":
#    evil_status = input(" Are you evil? \n ")
#    if evil_status == "Yes":
#     print(" you're not welcome here Evil Ben! \n")
#     exit()
# else:
#    print("\n Hello " + name + " ,thank you so much for coming in today \n\n\n")
# =============================================================================
# =============================================================================
# 
# name = input("What is your name? \n")
# 
# if name == "Ben":
#     evil_status = input("Are you evil? \n")
#     print(" You're not welcome here EVIL dooer! \n")
#     exit()
# else:
#     print("Hello"  + name + ",thank you for coming in \n\n\n")
# =============================================================================

# =============================================================================
# name = input()
# 
# if name == "Ben":
#     
#    evil_status = input("Are you evil? \n")
#    if evil_status == "Yes":
#        print("You're not welcome here Ben!! Get out")
#        exit()
#    else:
#        print("oh you're one of those good Bens. Come on in ")
# =============================================================================


#set a price for coffee 
order = input(":>")


if order == "Frap":
   price = 13
elif order == "Black_coffee":
    price = 3
elif order == "Espresso":
    price = 6
elif order == "Americano":
    price = 5
else:
    print("Sorry we do not have that here ")
    price = 0
       
  
 