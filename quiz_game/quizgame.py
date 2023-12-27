#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 06:59:36 2022

@author: latchy
"""

print("Welcome to my computer Quiz")

playing = input("\n Do you want to play a game?: ")

if playing.lower() != "yes":
    quit()
    
print("\n Okay! lets play :) ")
score = 0

answer = input("\n What does CPU stand for?: ")
if answer.lower() == "central processing unit":
        print('\n Correct!')
        score += 1
else:
    print("\n Incorrect!")
    
answer = input("\n What does GPU stand for?: ")
if answer.lower() == "graphic processing unit":
        print('\n Correct!')
        score += 1
else:
    print("\n Incorrect!")
    
answer = input("\n Wht is 2 + 2 =  ")
if answer.lower() == "4":
        print('\n Correct!')
        score += 1
else:
    print("\n Incorrect!")
    
print("You got " +str(score) + " Questions correct!")
print("\n You got " +str((score / 4) * 100) + "%. ")
    