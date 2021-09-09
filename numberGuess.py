#!/usr/bin/python3

# Write a program that randomly generates a number in the range of 0 to 9 and then prompts for a number. 
# The program should keep prompting until the user enters the randomly-generated number. 
# To generate a random number, put import random at the top and use random.randrange(10) 
# to generate a number in the range of 0 to 9. 
# Do not worry about invalid numbers for now.

import random

num = random.randrange(10)

guess = int(input('Pick a Number between 0 and 9\n')) # Assume a valid number

while num != guess:
    guess = int(input('Pick a Number between 0 and 9\n')) # Assume a valid number
