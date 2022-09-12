#!/usr/bin/python3

# Script: Ops 301 Class 09 Ops Challenge Solution
# Author: Jo Flow
# Date of latest revision: 9/11/2022
# Purpose: Python Collections (lists)

# Main

# Assign to a variable a list of ten string elements.
myFavThings = ["reading", "concerts", "partner", "family", "cats", "games", "boating", "shopping", "ramen"]

# display entire list
print(myFavThings)

#print the fourth element of the list
print(myFavThings[3])

#print the sixth through tenth element of the list
print(myFavThings[5:9])

#Change the value of the seventh element to “onion”
print(myFavThings)
myFavThings[7] = "onion"

print(myFavThings)