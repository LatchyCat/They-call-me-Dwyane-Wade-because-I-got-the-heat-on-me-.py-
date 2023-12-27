#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 07:37:07 2022
Edited on Wed, Dec/27/2023 :)
@author: latchy
New official @author: Count orie
"""

#Creating a anime list

from random import choice

animes = [['Naruto', 'pepehype', 'forever', 'series'],
         ['haikyuu', 'sports', 'short', 'series'],
         ['mushishi','chill', 'short', 'series'],
         ['One piece', 'epic', 'forever', 'series'],
         ['jojo', 'vampire', 'forever', 'series'],
         ['black clover', 'loud', 'mid lvl length', 'series']]


#input mood
print('what mood are you in?: ')
mood = input()

#Loop through and find the matching mood
for item in animes:
    if item[1] == mood:
        print(mood + ' anime: ' + item[0])

        import pandas
        pandas.__version__



# animes_df = pd.DataFrame(animes, columns = ['anime name', 'mood', 'length', 'type'])

# print("Watch this anime: " + choice(animes))
