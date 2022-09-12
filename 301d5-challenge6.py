#!/bin/python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author: Jo Flow
# Date of latest revision: 9/11/2022
# Purpose: Bash in Python


# import the operating system library
import os 
import subprocess

# import ipaddress

# use the os.system to call a bash command (source lecture)
os.system("ls")

print("This is introduction to using Python in bash")

#using subprocess method/source https://geekflare.com/python-run-bash/

import subprocess
subprocess.run(["whoami"])
print("This computer IP is `whoami` ")


