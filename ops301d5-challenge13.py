#!/usr/bin/python3

# Script: Ops 301 Class 12 Ops Challenge Solution
# Author: Jo Flow
# Date of latest revision: 9/15/2022
# Purpose: Python Requests Library

import requests

response = requests.get('https://github.com/Joflowcode')

print(response.status_code)

# ask user to pick which kind of htp method
# print menu of choices
# add conditional
# response put in variable
