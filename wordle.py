#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:33:52 2022

@author: viennathomas
"""
import random
word_list = open('/Users/viennathomas/Desktop/Not School/viennawordle/wordlist.txt').readlines()
mystery_number = random.randrange(5755)
mystery_word = word_list[mystery_number]
counter = 6
while counter >0: 
    guess = str(input("You have " +str(counter)+ " guesses left. Please Enter Your Word Guess: "))
    if len(guess)!=5: 
        print("Hey that doesn't have five letters bro...")
        break
    if guess == mystery_word:
        print(" Congrats! You have guessed the word correctly. It took you "+ str(6-counter)+" tries.")
    else:
        for i in range(5):
            if guess[i] in mystery_word:
                if guess[i] == mystery_word[i]:
                    print(guess[i]+" is in the correct position and is in the mystery word" )
                    i+=1
                else: 
                    print(guess[i]+" is not in the correct position but is in the mystery word")
                    i+=1
            else:
                print(guess[i]+" is not in the mystery word")
                i+=1
     #fix win condition           
            
    counter-=1
    if counter == 0 :
        print("You have run out of guesses. The word is " + mystery_word)
        counter = 6
        break