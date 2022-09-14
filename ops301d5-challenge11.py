#!/usr/bin/python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author: Jo Flow
# Date of latest revision: 9/14/2022
# Purpose: Python file handling. Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.


# create new text file

import os
from pdb import line_prefix  
os.mkdir("ops challenge 11")

file = open("challenge11.txt", "w")
file.write("This file is to be deleted")
file.close

## Need to figure out how to get mv process to work. import subprocess
# subprocess.run("mv challenge11.txt /home/jo/ops/301ops-challenges/ops challenge 11")

file = open("challenge11.txt", "a")
file.write("This is a new text file.")
file.close()

file = open("challenge11.txt", "a")
file.write("This is how you open the file created with the file name and w command.")
file.close()

file = open("challenge11.txt", "a")
file.write("You can use import os and import subprocess in file handling as well.")
file.close()

# this can be done with readline() for the first first line as well.
import linecache
lineRead = linecache.getline('challenge11.txt', 1)
print(lineRead)

# delete the text line.  source: https://www.w3schools.com/python/python_file_remove.asp
import os
os.remove("challenge11.txt")



# Stretch goal. Export pfsense config, edit code, save under new file. Then import new configs to pfsense. 

#opened config file in termnal and editor
file = open("config-vboxnet3pfSense.xml", "r")

file = open("newpfsenseconfigs.xml", "a")
file.write("The second task ran in this script was updating the pfsense config files. These new config settings are updating file 'config-vboxnet3pfsense.xml. The domain name was updated and also address pool was changed.") 


lineRead = linecache.getline('newpfsenseconfigs.xml', 289)
print(lineRead)
file.close()