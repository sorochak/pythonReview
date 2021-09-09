#!/usr/bin/python3

#Write a program that prompts for a water temperature and then prints out one of "Below freezing point", "Freezing point", or "Above freezing point", 
# depending on the entered temperature. Assume 0 as the freezing point. Do not worry about invalid numbers for now.

waterTemp = int(input('Water Temperature\n')) # Assume a valid number

if waterTemp < 0:
    print('Below freezing point')
elif waterTemp == 0:
    print('Freezing point')
else:
    print('Above freezing point')

