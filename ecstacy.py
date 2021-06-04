# !/usr/bin/python3

"""
author : Samora Machel
version: 1.0
github: https://github.com/SamoraMachel
"""


from configure import ENV_VAR
from colorama import Fore, Back, Style
import os, sys
import subprocess
import logging

from conf import promptStyle as shellprompt
from conf import GET_ENV
from lib.application.executor import execute

from lib.application.executor import execute


# dictionary for holding environment variables
ENV_VAR = GET_ENV()
MODE = 1

# the shell prompt style
# shell_prompt = shellprompt.hook()
command = "ecstacy"

# set the background of the terminal first 
# depending of the platform your in 
platform = sys.platform
if platform == "win32" :
    os.system("color a0")
elif platform == "linux" or platform == "linux2":
    os.system('setterm -background black -foreground white')

# function for executing commands depending of the mode
# the user is in 
# If the user is in Shell Mode then only comands that are recognized 
# by the system are executed 

def default_mode(command, spaced=True):
    # first we separate each item typed into the
    # terminal and feed the list to our program

    parsed_command = command.split(" ")
    if parsed_command[0] == 'shell':
        return 0
    elif parsed_command[0] == 'ecstacy':
        return 1 
    execute(parsed_command)
    if spaced:
        print()
    return 1

def shell_mode(command):
    parsed_command = command.split(" ")
    if parsed_command[0] == 'ecstacy':
        return 1
    elif parsed_command[0] == 'shell':
        return 0
    try: 
        subprocess.call(parsed_command)
        print()
    except Exception:
        default_mode(command)
    return 0
    

print(Style.RESET_ALL, Fore.RESET)
while(command != "exit") :    
    
    if MODE == 1 and command:
        MODE = default_mode(command)
    elif MODE == 0 and command:
        MODE = shell_mode(command)
    prompt = shellprompt.hook(MODE)
    command  = str(input(prompt))
    print(Style.RESET_ALL, Fore.RESET)
    
    
    