#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:15:35 2022

@author: rhodadurodola
"""

import random
print("Welcome to Nim.")

def start():
    coinlist = []
    piles = random.randint(2, 4)
    coins = random.randint(1, 10)
    player1, player2 = get_players()

    currentplayer = player1 # player 1 starts first
    
    initialsetup(coinlist, piles, coins, currentplayer) 

    newgame(coinlist, piles, coins, player1, player2, currentplayer) 

def get_players():
    return input("Player 1 Name: "), input("Player 2 Name: ")

#printing a randam set of piles of coins for the player
def initialsetup(coinlist, piles, coins, currentplayer):
    for i in range(0, piles):
        coins = random.randint(1, 7)
        print('Pile {}: {}'.format(i + 1, 'o' * coins))
        coinlist.append(coins)


def inputcheck(coinlist, piles, currentplayer):

    #loop that makes sure player 1 enters a valid input 
    #(will keep asking if they haven't)
    #ctr = coins to remove, ptrf = piles to remove from
    while True:
        ctr = input\
            ('How many coins do you want to remove {}? '.format(currentplayer))
        ptrf = input('Choose a pile to remove this from: ')

        #loop is broken if all the conditions are satisfied:
        if (ctr and ptrf) and (ctr.isdigit()) and (ptrf.isdigit()): 
            if (int(ctr) > 0) and (int(ptrf) <= len(coinlist)) and \
                (int(ptrf) > 0):
                if (int(ctr) <= coinlist[int(ptrf) - 1]):
                    if (int(ctr) != 0) and (int(ptrf) != 0):
                        break
        #does this if conditions aren't met
        print("Try again as you entered an invalid value") 
        
    # updates the new coinlist from whichever pile is chosen
    coinlist[int(ptrf) - 1] -= int(ctr)
    #shows new piles after current player moves
    cont(coinlist, piles, currentplayer) 

def cont(coinlist, piles, currentplayer): 
    for i in range(0, piles):
        print("Pile {}: {}".format(i + 1, 'o' * coinlist[i]))

# prints loser of game form who took last coin (misere play), 
# asks if players want to play game again,
def newgame(coinlist, piles, coins, player1, player2, currentplayer):
    # loop allows players to keep starting a new game
    while True:
        inputcheck(coinlist, piles, currentplayer)        
        if coinlist == [0] * len(coinlist):
            print("Oh no you took the last coin.")
            print("Better luck next time {}. ".format(currentplayer))
            print("Would you like to play again?")
            user = input("Enter Y if Yes and anything else if No: ")

            if user.upper() == 'Y':
                start()            
            else:
                break
            
        # players can take turns
        if currentplayer == player1:
            currentplayer = player2

        else:
            currentplayer = player1

start()

