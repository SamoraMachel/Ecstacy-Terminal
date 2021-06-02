# !/usr/bin/python3

"""
author : Samora Machel
version: 1.0
github: https://github.com/SamoraMachel
"""


from configure import ENV_VAR
from colorama import Fore, Back, Style
import os, sys
import sys
import logging

from conf import promptStyle as shellprompt
from conf import GET_ENV
from lib.application.executor import execute

from lib.application.executor import execute

# dictionary for holding environment variables
ENV_VAR = GET_ENV()

# the shell prompt style
shell_prompt = shellprompt.hook()
command = str(input(shell_prompt))

# set the background of the terminal first 
# depending of the platform your in 
platform = sys.platform
if platform == "win32" :
    os.system("color a0")
elif platform == "linux" or platform == "linux2":
    os.system('setterm -background black -foreground white')

# intialize the terminal object
# terminalObject = Terminal()

print(Style.RESET_ALL, Fore.RESET)
while(command != "exit") :    
    # first we separate each item typed into the
    # terminal and feed the list to our program
    parsed_command = command.split(" ")

    execute(parsed_command)
    print()
    prompt = shell_prompt
    command  = str(input(prompt))
    print(Style.RESET_ALL, Fore.RESET)

    