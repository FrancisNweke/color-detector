# -*- coding: utf-8 -*-
from numpy import random
"""
Created on Sun Feb  9 14:13:23 2020

@author: Nweke Francis
"""

def pickNumberRandomly():
    choices = list(range(10000))
    random.shuffle(choices)
    print("generated number:", choices.pop())
    
    retry = None #retry set to none
    while retry not in ('y','n'):       
        retry = input("want another random number?(Y/N): ")
        if retry.lower() == 'n':
           break
        elif retry.lower() == 'y':
           randomGenerator()
           break
        else:
           print("please enter y/n.")
        #print("generated number:", choices.pop())


def randomGenerator():
    x = random.rand(3)   #use rand: floating numbers or use randint: integers
    print("generated number(s):", x)
                    

#randomGenerator()
pickNumberRandomly()
