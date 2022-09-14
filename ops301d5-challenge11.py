#!/usr/bin/python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author: Jo Flow
# Date of latest revision: 9/14/2022
# Purpose: Python file handling. Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.


# create new text file

import os  
os.mkdir("ops challenge 11")

file = open("challenge11.txt", "w")
file.write("This is a new text file")
file.close

import subprocess
subprocess.run(mv challenge1)

file = open("challenge11.txt", "a")
file.write("This file is to be deleted.")
file.close()

file = open("challenge11.txt", "a")
file.write("This is how you open the file created with the file name and w command.")
file.close()

file = open("challenge11.txt", "a")
file.write("You can use import os and import subprocess in file handling as well.")
file.close()

file = open("challenge.txt", "r")
print(file.readline())






# Stretch goal. Export pfsense config, edit code, save under new file. Then import new configs to pfsense. 

file = open("config-vboxnet3pfSense.xml", "r")
print(file.read())

file = open("newpfsenseconfigs.xml", "w")

file = open("newpfsenseconfigs.xml", "a")
file.write("These new config settings are updating file 'config-vboxnet3pfsense.xml. The domain name was updated and also address pool was changed.") 
file.close()

file = open("newpfsenseconfigs.xml")
print(file.read())


