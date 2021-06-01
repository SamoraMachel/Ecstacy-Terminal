from colorama import Fore, Back, Style
import os
import getpass

# hook like prompt style
def hook():
    path = Fore.YELLOW + os.path.basename(os.getcwd())
    user = Fore.YELLOW + getpass.getuser()

    # the settings can be modified to suit users needs

    firstPart = Fore.WHITE + "┌─"
    lastPart = Fore.WHITE + "└──╼"
    RightBracket = Fore.WHITE + "─["
    LeftBracket = Fore.WHITE + "]"
    dash = Fore.WHITE + "─"

    # shell prompt 
    return f"{firstPart}{RightBracket}{user}{LeftBracket}{dash}{RightBracket}{path}{LeftBracket}\n{lastPart} # "