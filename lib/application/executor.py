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

def execute(**args):
    command_file = COMMANDS.get(args[0], False);
    if command_file == False:
        raise EcstacyException().InvalidCommand(args[0])


