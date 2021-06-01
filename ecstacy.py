from colorama import Fore, Back, Style
import os
import sys
import logging

from conf import promptStyle as shellprompt



prompt = shellprompt.hook()
command = str(input(prompt))

# set the background of the terminal first 
# depending of the platform your in 
platform = sys.platform
if platform == "win32" :
    os.system("color a0")
elif platform == "linux" or platform == "linux2":
    os.system('setterm -background black -foreground white')

# intialize the terminal object
terminalObject = Terminal()

print(Style.RESET_ALL, Fore.RESET)
while(command != "exit") :
    # first we have to parse the commands given
    # in order to identify the parent command

    parsedCommand = command.split(" ")
    # we have to update the path of the prompt each time 
    # a command is executed
    path = Fore.YELLOW + os.path.basename((terminalObject.getCurrentPath())) or  '~'
    prompt = shellprompt.hook()
    command  = str(input(prompt))
    print(Style.RESET_ALL, Fore.RESET)

    