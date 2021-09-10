#!/usr/bin/python3

# Modify the prime checker so that it also prints out if the input is not a number

try:

    num = int(input('Enter a number:\n')) # Assume int > 1 

    i = 2
    prime = True

    while i * i <= num:
        if num % i == 0:
            print(str(num) + ' is not a prime')
            prime = False
            break
        i=i+1
        
    if prime:
    print(str(num) + ' is a prime')



except ValueError:
    print('Your input is not a valid number')
    