# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:59:05 2024

@author: santo
"""
import random

# Function to randomly pick a word from a predefined list
def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 'mathematics', 'solution']
    pick = random.choice(words)
    return pick

# Function to jumble the picked word
def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))  # Randomly shuffle letters of the word
    return jumbled

# Function to thank the players and show the final score
def thank(p1n, p2n, p1, p2):
    print(p1n, 'your score is : ', p1)
    print(p2n, 'your score is : ', p2)
    print('Thanks for playing')
    print('Have a nice day')

# Main game function
def play():
    p1_name = input('player1, please enter your name: ')  # Get Player 1 name
    p2_name = input('player2, please enter your name: ')  # Get Player 2 name
    pp1 = 0  # Player 1 score
    pp2 = 0  # Player 2 score
    turn = 0  # Variable to track whose turn it is

    while True:  # Infinite loop to keep the game going until a player decides to quit
        picked_word = choose()  # Get a random word
        qn = jumble(picked_word)  # Get a jumbled version of the word
        print(qn)  # Display the jumbled word

        if turn % 2 == 0:  # If it's player 1's turn (even turn number)
            print(p1_name, 'your turn')
            ans = input('What is on my mind?: ')  # Player 1 guesses the word
            if ans == picked_word:  # If the guess is correct
                pp1 += 1  # Increase player 1's score
                print('Your score is: ', pp1)
            else:
                print('Better luck next time, I thought: ', picked_word)
            c = input('Press 1 to continue and 0 to quit: ')  # Ask if they want to continue or quit
            if c == '0':  # If player wants to quit
                thank(p1_name, p2_name, pp1, pp2)  # Display final scores and exit
                break
        else:  # If it's player 2's turn (odd turn number)
            print(p2_name, 'your turn')
            ans = input('What is on my mind?: ')  # Player 2 guesses the word
            if ans == picked_word:  # If the guess is correct
                pp2 += 1  # Increase player 2's score
                print('Your score is : ', pp2)
            else:
                print('Better luck next time, I thought: ', picked_word)
            c = input('Press 1 to continue and 0 to quit: ')  # Ask if they want to continue or quit
            if c == '0':  # If player wants to quit
                thank(p1_name, p2_name, pp1, pp2)  # Display final scores and exit
                break

        turn += 1  # Increment the turn number after each round

# Start the game
play()
