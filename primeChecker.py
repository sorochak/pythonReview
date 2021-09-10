#!/usr/bin/python3

num = int(input('Enter a number:\n')) # Assume int > 1 

i = 2

while i * i <= num:
    if num % i == 0:
        print(str(num) + ' is not a prime') 
        break
    else:
        print(str(num) + ' is a prime')

i=i+1