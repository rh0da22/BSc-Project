#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:20:05 2022

@author: rhodadurodola
"""

import random

stonesLeft = random.randint(15, 30)
stonesToRemove = 0
userTurn = True

print("This is a game where players take turns taking stones from a pile of stones. The player who takes the last stone loses. The current stone count is: ", stonesLeft)

while stonesLeft > 0:
    while userTurn == True and stonesLeft > 0:

        stonesToRemove = int(input("How many stones do you want to remove?"))

        if stonesToRemove > 3:ArithmeticError
            print("You can't remove more than three stones at a time! 
                The current stone count is: " + str(stonesLeft) )     
        elif stonesLeft - stonesToRemove < 0:
            print("There aren't that many stones left!") #Give user error!  
        else:
            stonesLeft -= stonesToRemove
            print( "You removed " + str(stonesToRemove) + 
                " stone(s)! The current stone count is: " + str(stonesLeft) )    

            userTurn = False                       

    while userTurn == False and stonesLeft > 0:

        aiRemoves = random.randint( 1, min(3, stonesLeft) ) #Take smaller value between 3 and the stones that are left
        stonesLeft -= aiRemoves

        print( "The A.I. removed " + str(aiRemoves) + 
            " stone(s)! The current stone count is: " + str(stonesLeft) )    

        userTurn = True 

if userTurn == True:
    print("The A.I took the last stone, it lost. You won the game!")
else:
    print("You took the last stone, you lost. The A.I. won the game!")