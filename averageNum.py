#!/usr/bin/python3

#Write a program that prints out 100 random numbers (each in the range of 0 to 99), 
# then computes and prints out the average of them.

import random

avg = 0

for i in range(100):
    num = random.randrange(100)
    avg += num
    print(str(num))

print(str(avg / 100))