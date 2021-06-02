from colorama import Fore, Style

class EcstacyException(BaseException):

    # invoked when a certain command doesn't
    # contain a certain attribute
    def InvalidCommandAttribute(self, command, attrib):
        print(Fore.RED + Style.BRIGHT + "×", end="")
        print(Fore.WHITE + Style.NORMAL + " ecstacy: ", end="")
        print(Fore.RED + Style.NORMAL + command , end="") 
        print(Fore.LIGHTBLACK_EX + f": invalid command argument ", end="")
        print(Fore.RED + attrib)
        print(Style.RESET_ALL, Fore.RESET)

    # invoked when a non-existant command is
    # called
    def InvalidCommand(self, command):
        print(Fore.RED + Style.BRIGHT + "×", end="")
        print(Fore.WHITE + Style.NORMAL + " ecstacy: ", end="")
        print(Fore.RED + Style.NORMAL + command, end="") 
        print(Fore.LIGHTBLACK_EX + " is not a command")
        print(Style.RESET_ALL, Fore.RESET)

