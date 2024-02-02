#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 01:08:53 2022

@author: rhodadurodola
"""

import random

coins = random.randint(1, 15)
piles = random.randint(2, 5)
coinstoremove = 0
playermove =  True

print("This is a game where players take turns taking stones from a pile of coin0. The player who takes the last scoin loses. The current coin count is: ",coins)

while coins > 0:
    while playermove == True and coins > 0:
        coinstoremove = int(input("How many coins do you want to remove? Type in the number: "))
        if coins - coinstoremove < 0:
            print("There aren't enough coins to remove that many!") + str(coins)
        else:
            coins -= coinstoremove
            print("There are now " + str(coins) + " coins left.")
            playermove = False
            
    while playermove == False and coins > 0:

        computer = random.randint( 1, min(3, coins) ) 
        coins -= computer
        

        print( "The computer removed " + str(computer) + " coin(s)! There are now " + str(coins) + " coins left.")   

        playermove = True 

if playermove == True:
    print("The computer took the last coin so you won!")
else:
    print("You took the last stone, you lost :(")















