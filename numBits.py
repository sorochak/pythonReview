#!/usr/bin/python3

# Write a program that prompts for a number and then prints out the number of bits in that number. 
# For example, 10 has 2 bits in it. 
# Assume the number is valid.


num = int(input('Enter and integer\n')) # Assume a valid number
count = 0

while(num != 0):
    count += num & 1
    num >>= 1
print(count)

