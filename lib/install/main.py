# !/usr/bin/env python3
import cli
import shutil
import os
from lib.application.exceptions import EcstacyException

class install(cli.app.CommandLineApp):
    name = "install" 
    description = "Used to install an application into Esctacy"

    # holds the commands and thier location
    def __init__(self) -> None:
        super().__init__()
        self.commands = []

    def main(self):
        with open('conf/commands.conf') as ConfComm:
            commands = ConfComm.readlines()

    # saves the list of commands added in the self.command list
    def save_commands(self):
        with open('conf/commands.conf', 'a') as ConfComm:
            for command in self.commands:
                ConfComm.write(f"{command[0]}\t\t{command[1]}\n")
    
    # gets the installable folder and copies it to 
    # the right lib folder
    def copy_command(self, folder):
        from conf import GET_ENV

        relative_path = GET_ENV()['PATH']
        destination_folder = os.path.join(relative_path, 'lib')
        shutil.copy(folder, destination_folder)

    # gets the installable folder and moves it to 
    # the right lib folder
    def move_command(self, folder):
        from conf import GET_ENV

        relative_path = GET_ENV()['PATH']
        destination_folder = os.path.join(relative_path, 'lib')
        shutil.move(folder, destination_folder)

    # checks if it is a valid installable folder
    def check_folder(self, folder):
        # check if the file location exists first of all
        # also check if its a folder
        if os.path.exists(folder) == False:
            return EcstacyException.NonExistantPath(folder)
        
        if os.path.isdir(folder) == False:
            return EcstacyException.NonInstallable(folder)

        # check if is is an installable folder
        executable_file = os.path.join(folder, 'main.py')
        if os.path.exists(executable_file) == False:
            return EcstacyException.NonInstallableFolder(folder)

        return True


            

if __name__ == '__main__':
    install().run()