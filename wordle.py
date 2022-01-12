#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:33:52 2022

@author: viennathomas
"""
import random
word_list = open('/Users/viennathomas/Desktop/Not School/viennawordle/wordlist.txt').readlines()
mystery_number = random.randrange(5755)
#mystery_word = word_list[mystery_number]
mystery_word = 'quark'
counter = 6
starting_blanks= ['_','_','_','_','_']
end = True

if counter == 0 :
    print("You have run out of guesses. The word is " + mystery_word)
    end = False
    counter = 6
    
while end is True : 
    while counter > 0:
        print ("\n The word so far is: \n")
        print(*starting_blanks, sep= ' ')
        guess = str(input("You have " +str(counter)+ " guesses left. Please Enter Your Word Guess: "))
        number_correct_letters = 0
        if len(guess)!=5: 
            print("Hey that doesn't have five letters bro...")
        else:
#    if guess not in word_list:
#        print("Come on... that's not a word... Try again")
#        break 
        #dk how to get this to work
            if guess == mystery_word:
                    print(" Congrats! You have guessed the word correctly. It took you "+ str(7-counter)+" tries.")
                    end = False
                    break
            else:
                for i in range(5):
                    if guess[i] in mystery_word:
                       
                        if guess[i] == mystery_word[i]:
                            starting_blanks[i] = guess[i]
                            number_correct_letters+=1
                            print(guess[i]+" is in the correct position and is in the mystery word" )
                            i+=1
                            if number_correct_letters == 5:
                                print(" Congrats! You have guessed the word correctly. It took you "+ str(7-counter)+" tries.")
                                break 
                        else: 
                            print(guess[i]+" is not in the correct position but is in the mystery word")
                            i+=1
                    else:
                        print(guess[i]+" is not in the mystery word")
                        i+=1          
        counter-=1
