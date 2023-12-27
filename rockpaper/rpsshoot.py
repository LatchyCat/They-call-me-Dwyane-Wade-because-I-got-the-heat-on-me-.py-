#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 08:16:36 2022

@author: latchy
"""

import random
def play():
    
    user = input = ("Whats your choice? 'r' for rock, 'p' ,for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer :
        return "It's a tie"
    
    #r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    return 'you lost'

    def is_win(player, oppenent):
        #Returns true if player wins 
        #r > s, s > p, p > r
        if (player == 'r' and oppenent == 's') or (player == 's' and oppenent == 'p') or (player == 'p' and oppenent == 'r'):
            return True
        
        print(play())