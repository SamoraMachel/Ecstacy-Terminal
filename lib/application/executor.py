# !/usr/bin/python3

"""
author : Samora Machel
version: 1.0
github: https://github.com/SamoraMachel
"""

# this module does the work of execution of the commands
# it calls each command and maps it to the equivalent 
# python execution file

from conf import GET_COMMANDS
from lib.application.exceptions import EcstacyException


COMMANDS = GET_COMMANDS()

def execute(parsed_command):
    command_file = COMMANDS.get(parsed_command[0], False);
    if command_file == False:
        return EcstacyException().InvalidCommand(parsed_command[0])

