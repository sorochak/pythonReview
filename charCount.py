#!/usr/bin/python3

# Write a function that accepts a string and then tallies how often a character appears,
# and only returns the character that appears most often

from collections import Counter

s = input('Enter a string:\n')

def charMaxFreq(s):
    maxChar = Counter(s)
    maxChar = max(maxChar, key = maxChar.get)
    return maxChar

charMaxFreq(s)