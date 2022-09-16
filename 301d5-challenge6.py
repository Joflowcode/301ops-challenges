#!/bin/python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author: Jo Flow
# Date of latest revision: 9/11/2022
# Purpose: Bash in Python


# import the operating system library
import os 
import subprocess


# use the os.system to call a bash command (source lecture)
import os
os.system("ls")
# print('ls /home/jobuntu/301ops-challenges')
path = '/home/jobuntu/301ops-challenges'

print("This the list of all the contents in the 301ops challenge directory")

#using subprocess method/source https://geekflare.com/python-run-bash/

import subprocess
subprocess.run(["whoami"])


