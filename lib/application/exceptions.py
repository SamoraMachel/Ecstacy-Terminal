from colorama import Fore, Style
import os
class EcstacyException(BaseException):

    # invoked when a certain command doesn't
    # contain a certain attribute
    def InvalidCommandAttribute(self, command, attrib):
        print(Fore.RED + Style.BRIGHT + "×", end="")
        print(Fore.WHITE + Style.NORMAL + " ecstacy: ", end="")
        print(Fore.RED + Style.NORMAL + command , end="") 
        print(Fore.LIGHTBLACK_EX + f": invalid command argument ", end="")
        print(Fore.RED + attrib)
        print(Style.RESET_ALL, Fore.RESET, end="")

    # invoked when a non-existant command is
    # called
    def InvalidCommand(self, command):
        print(Fore.RED + Style.BRIGHT + "×", end="")
        print(Fore.WHITE + Style.NORMAL + " ecstacy: ", end="")
        print(Fore.RED + Style.NORMAL + command, end="") 
        print(Fore.LIGHTBLACK_EX + " is not a command")
        print(Style.RESET_ALL, Fore.RESET, end="")

    # invoked when a non-existant file or folder is passed
    def NonExistantPath(self, path):
        print(Fore.RED + Style.BRIGHT + "×", end="")
        print(Fore.WHITE + Style.NORMAL + " ecstacy: ", end="")
        print(Fore.RED + Style.NORMAL + path, end="")
        print(Fore.LIGHTBLACK_EX + " does not exists")
        print(Style.RESET_ALL, Fore.RESET, end="")
    
    def NonInstallableFolder(self, path):
        print(Fore.RED + Style.BRIGHT + "×", end="")
        print(Fore.WHITE + Style.NORMAL + " ecstacy: ", end="")
        print(Fore.RED + Style.NORMAL + os.path.dirname(path), end="")
        print(Fore.LIGHTBLACK_EX + " is not an installable folder, missing the main.py")
        print(Style.RESET_ALL, Fore.RESET, end="")

    def NonInstallable(self, path):
        print(Fore.RED + Style.BRIGHT + "×", end="")
        print(Fore.WHITE + Style.NORMAL + " ecstacy: ", end="")
        print(Fore.RED + Style.NORMAL + path, end="")
        print(Fore.LIGHTBLACK_EX + " is a file, expected an installable folder")
        print(Style.RESET_ALL, Fore.RESET, end="")

