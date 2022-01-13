#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:33:52 2022

@author: viennathomas
"""
import os
import random

def grid_maker(guesses):
    grid= []
    for i in range(guesses):
        grid.append(['_','_','_','_','_'])
    return grid
def print_grid(grid):
    for grid_line in grid:
        print(*grid_line, sep= ' ')

def convert(mystery_word):
    correct_word=[]
    correct_word[:0]=mystery_word
    return correct_word
           
def game_start():
    dir = os.path.dirname(__file__)
    with open(os.path.join(dir, 'wordlist.txt'), 'r') as f:
        word_list = [word.strip() for word in f.readlines()]
#    mystery_word = 'stale'
    mystery_word = random.choice(word_list)
    game_play(mystery_word, word_list)
    play_again()
   
def game_play(mystery_word,word_list):
    mystery_word_list = convert(mystery_word)
    grid = grid_maker(6)
    print_grid(grid)  
    counter = 0
    while counter <6:
        guess = input("You have " +str(6-counter)+ " guesses left. Please Enter Your Word Guess: ") 
        if guess == mystery_word:
            print("\n nice. you won in "+ str(counter+1)+' tries.')
            return
        if len(guess)!=5: 
            print("Hey that doesn't have five letters bro...")
        elif guess not in word_list:
            print("Come on... that's not a word... Try again")
            
            
        else:
            thing_list = mystery_word_list.copy()
            for i in range(len(guess)):
                
                
                if guess[i] == mystery_word[i]:
                    grid[counter][i] = guess[i].upper()
                    thing_list.remove(guess[i])
                    print(guess[i]+" is  in the correct position and is in the mystery word.\n")
                    
                elif guess[i] in thing_list:
                    grid[counter][i] = guess[i]
                    thing_list.remove(guess[i])
                    print(guess[i]+" is not in the correct position but is in the mystery word.\n")
                else:
                    grid[counter][i] = guess[i]
                    print(guess[i]+ " is not in the mystery word.\n")
            print_grid(grid)
            counter += 1
    print ("\n you suck. the word is " + mystery_word)
    
    
#def colours():
#
def play_again():
    more_game = input('Do you want to play again or are you sick of this game? Y/N? ')
    if more_game.lower() == 'y':
        game_start()
    
    
#    
    
game_start()

