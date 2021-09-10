#!/usr/bin/python3

num = int(input('Enter a number:\n')) # Assume int > 1 

i = 2
prime = True

while i * i <= num:
    print(i)
    if num % i == 0:
        print(str(num) + ' is not a prime') 
        prime = False
        break
    i=i+1

if prime:
    print(str(num) + ' is a prime')


