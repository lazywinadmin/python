# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables
    global secret_number,remaining_guess
    secret_number = 0
    guesses = 0
    
    # Start Frame
    frame.start()
    
    #Default Range is 100
    range100()


# define event handlers for control panel
def range100():
    # Global variables
    global secret_number, guesses
    guesses = 7
    
    # Set a secret number
    secret_number = random.randrange(0, 101)
    
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is", guesses
    print

def range1000():
    # Global variables
    global secret_number
    guesses = 10
    
    # Set a secret number
    secret_number = random.randrange(0, 1001)
    
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is", guesses
    print
    
def input_guess(guess):
    # Global variables
    global guesses
    
    # Remove a guess from guesses
    guesses -= 1
    
    # Convert guess text to integer
    guess = int(guess)
    
    print "Guess was", guess
    print "Number of remaining guesses is", guesses
    
    if guess == secret_number:
        print "Correct!"
        print
        range100()
        
    elif guess < secret_number:
        print "Higher!"
        
    else:
        print "Lower!"

    if guesses == 0:
        print "No more guesses available!"
        print
        range100()
    print
    
# Create frame
frame = simplegui.create_frame('Guess the number', 300,200)

# Register Event Handlers for control elements
frame.add_button('Range is [0, 100]', range100,200)
frame.add_button('Range is [0, 1000]', range1000,200)
frame.add_input('Enter a Guess', input_guess, 200)

# Call a new_game 
new_game()