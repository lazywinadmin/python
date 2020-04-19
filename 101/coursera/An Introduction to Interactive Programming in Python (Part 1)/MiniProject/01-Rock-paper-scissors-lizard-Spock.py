# "An Introduction to Interactive Programming in Python"
# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# Import Module
import random

# Helper Functions
def name_to_number(name):
   
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "no name specified"
  
def number_to_name(number):
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "no number specified"

# Main Function
def rpsls(player_choice): 
    # Print out the message for the player's choice
    print "Player chooses", player_choice
    
    # Convert the player's choice to player_number using the function name_to_number()
    var_number = name_to_number(player_choice)

    # Compute random guess for comp_number using random.randrange()
    # you actually need to specify until 5, but the possiblities are 0 1 2 3 4 (not 5)
    var_comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    var_comp_choice = number_to_name(var_comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", var_comp_choice
    
    # compute difference of comp_number and player_number modulo five
    var_diff = (var_comp_number - var_number) % 5

    # Debug
    """
    print "var_diff is",var_diff
    print "var_comp_number is",var_comp_number
    print "var_number is",var_number
    """
    
    # use if/elif/else to determine winner, print winner message
    if var_diff > 2:
        print "Player wins!"
    elif (var_diff > 0 and var_diff <= 2):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    
    
    # Add white space/Blank line
    print ""
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



