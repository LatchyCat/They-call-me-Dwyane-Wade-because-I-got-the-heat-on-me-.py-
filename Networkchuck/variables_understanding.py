#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 07:12:16 2022

@author: latchy
"""

# =============================================================================
# #Building a robot Barista #Trial 1
# 
# print("Hello, Welcome to Latchy's coffee shop")
# 
# # input("What is your name? \n >")
# 
# # print(input("What is your name? \n >"))
# 
# name = input("What is your name? \n: ")
# 
# print("Hello " + name + " Thank you for coming in the shop")
# # print("Hello! Thank you so much for coming in today.")
# 
# menu = "Black coffee, Espresso, Latte, Capachino"
# 
# print(name + " What would you like from our menu today?  \n Here is what we're serving. \n" + menu)
# 
# order = input(":")
# 
# print("Sounds great " + name + " I will have your " + order + " Out in a Jiffy")
# =============================================================================

# =============================================================================
# #Building a robot Barista #Trail 2 = Clean up
# 
# print("Hello, Welcome to Latchy's coffee shop \n")
# 
# name = input("What is your name? \n:> ")
# 
# #################################################################1
# 
# print("\n Hello " + name + " \n\n Thank you for coming into the Latchy's mystery brews \n\n")
# 
# menu = "\n Black coffee, Espresso, Latte, Capachino\n"
# 
# print(name + " \n \n What would you like from our menu today?  \n\n Here is what we're serving. \n" + menu)
# 
# #################################################################2
# 
# order = input(":>")
# 
# price = 8
# 
# quantity = input("\n How many coffees would you like? \n")
# 
# total = price * int(quantity)
# 
# print("Thank you, your total is: " + str(total)
# 
# #print("Sounds great " + name + " I will have your " + order + " out in a Jiffy")
# 
# ################################################################3
# =============================================================================



#Building a robot barista #Trail 3 = why wont it work 

# =============================================================================
# #Part 1
# =============================================================================

print("Hello good sir!, \n\n Welcome to Lord Latchy's Smean to your face coffee shop")

name = input(("\n\n What is your name?! :>"))


# =============================================================================
# #part 2 / If and else statments
# =============================================================================

#print("Hello Sir and welcome to coffee hut \n\n ")

if name == "Ben":
   evil_status = input("Are you evil? \n")
if evil_status == "Yes":
    print(" You're not welcome here EVIL dooer! \n")
    exit()
else:
    print("Oh you're one of those good Bens. Come on it! \n") 

# =============================================================================
# #Part 3
# =============================================================================

print("\n\n Pick what you want already! " + name + "\n\n")

menu = "\n\n Black_coffee, Espresso, Americano, Frap \n"

print(name + " this is what is on our menu, Pick fast I got places to be! GRRRR \n\n" + menu)

extra_menu = "\n\n Caramel_Frap, whipped_cream_Frap, Banana \n"

print("Theses are our sides By the way \n\n " + extra_menu)

# =============================================================================
# #Part 4
# =============================================================================

order = input(":>")

if order == "Frap":
   price = 13
elif order == "Caramel_Frap":
    price = 15
elif order == "whipped_cream_Frap":
    Price = 12
elif order == "Black_coffee":
    price = 3
elif order == "Espresso":
    price = 6
elif order == "Americano":
    price = 5
elif order == "Banana":
    price = 100
else:
    print("Sorry we do not have that here ")
    price = 0

quantity = input("\n\n  Ughhh ... how many coffees would you like? \n :>" )

total = price * int(quantity)

print("\n\n\ Muhahah your total is :> $" + str(total))

# =============================================================================
# #part 5 
# =============================================================================

