from colorama import Fore, Back, Style
import os
import getpass

# hook like prompt style
def hook(mode=1):
    # mode 1 - Normal Ecstacy shell mode
    # mode 0 - default system shell mode
    path = Fore.YELLOW + os.path.basename(os.getcwd())
    user = Fore.YELLOW + getpass.getuser()

    # the settings can be modified to suit users needs

    firstPart = Fore.WHITE + "┌─"
    lastPart = Fore.WHITE + "└──╼"
    RightBracket = Fore.WHITE + "─["
    LeftBracket = Fore.WHITE + "]"
    dash = Fore.WHITE + "─"
    shellmode = Fore.WHITE + "(" + Fore.RED + "shell" + Fore.WHITE + ")"
    

    # shell prompt 
    if mode == 1:
        return f"{firstPart}{RightBracket}{user}{LeftBracket}{dash}{RightBracket}{path}{LeftBracket}\n{lastPart} # "
    elif mode == 0:
        return f"{firstPart}{RightBracket}{user}{LeftBracket}{dash}{RightBracket}{path}{LeftBracket}{dash}{shellmode}\n{lastPart} # "