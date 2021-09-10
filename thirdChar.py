#!/usr/bin/python3

# Write a program that prompts for a string and then prints out every 3rd character of that string

s = input('Enter a string:\n')

for i in range(2, len(s), 3):
    print(s[i])