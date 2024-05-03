## START OF FILE ##
import os
import random
from time import sleep
from colorama import Fore, Style


def clear() -> None:
    os.system("clear")
    #clears anything already on the screen
#More style options for console text:
RESET: str = "\u001B[0m"
BLACK: str = "\u001B[30m"
RED: str = "\u001B[31m"
GREEN: str = "\u001B[32m"
YELLOW: str = "\u001B[33m"
BLUE: str = "\u001B[34m"
MAGENTA: str = "\u001B[35m"
CYAN: str = "\u001B[36m"
BACK_RED: str = "\u001B[41m"
BACK_GREEN: str = "\u001B[42m"
BACK_YELLOW: str = "\u001B[43m"
BACK_BLUE: str = "\u001B[44m"
BACK_MAGENTA: str = "\u001B[45m"
BACK_CYAN: str = "\u001B[46m"
BACK_WHITE: str = "\u001B[47m"
BOLD: str = "\u001B[1m"
UNDERLINE: str = "\u001B[4m"
ITALIC: str = "\u001B[3m"
STRIKETHROUGH: str = "\u001B[9m"
TAB = "\t"

#fallback
skipping = None
#fun rgb functions:
def RGB(r: int, g: int, b: int) -> str:
    return "\x1b[382" + str(r) + "" + str(g) + "" + str(b) + "m"


def BACK_RGB(r: int, g: int, b: int) -> str:
    return "\x1b[482" + str(r) + "" + str(g) + "" + str(b) + "m"


# color for the player
BRIGHT_YELLOW: str = RGB(255, 255, 0)
# color for developer text
BRIGHT_GREEN: str = RGB(0, 255, 0)
# color for the shadow
SHADOW_PURPLE: str = RGB(223, 0, 255)
# color for the mothership
MOTHERSHIP_GREEN: str = RGB(75, 255, 75)
#moved to the top


def printS(text: str, color: str = "", delay: float = 0.01, newline: bool = False, loader: bool = False) -> None: # slow print function

    '''print function that prints slowly because yes. artistic license(???)
    now shut up you critics
    Input: text, color, delay => text but colored, and delay'''
    print(color, end="", flush=True)
    for i in text:
        try:
            print(i+color, end="", flush=True)
            if not skipping:
                sleep(delay)
                match i:
                    case "\n":
                        if loader:
                            sleep(delay)
                        else:
                            sleep(0.4+delay)
                    case ".":
                        sleep(0.2+delay)
                    case ",":
                        sleep(0.1+delay)
                    case _:
                        sleep(delay)    
            if bool(color):
                print(Style.RESET_ALL, end="", flush=True)
            if(newline):
                print() #deal with it


        except KeyboardInterrupt:
            delay = 0

    print() #gives newline *and* style reset!

def printD(text: str, talker: str="Prism", color: str = "", delay: float = 0.02):
    '''Print function specialized for dialouge
    Input: text, talker --> Talker: text'''

    if talker.strip().lower() == "developers" or talker.strip().lower() == "developer":
        to_print = BRIGHT_GREEN+BOLD+talker+": "+Style.RESET_ALL
    elif talker.strip().lower()=="???":
        to_print = Fore.MAGENTA+Style.BRIGHT+BOLD+talker+": "+Style.RESET_ALL
    elif (talker.strip().lower() == "developers + prism"):
        to_print = BRIGHT_GREEN+BOLD + "Developers" + Style.RESET_ALL + " and "+ Fore.BLUE + BOLD + "Prism" ": " + Style.RESET_ALL
    elif (talker.strip().lower() == "omegagodzilla66" or talker.strip().lower() == "computingsquid"):
        to_print = Fore.YELLOW + BOLD + talker + ": " + Style.RESET_ALL
    else: 
        to_print = Fore.BLUE+BOLD+talker+": "+Style.RESET_ALL
    printS(to_print + text,color,delay)


# end of slow print function

def printCS(text: str, cColor: str, color: str = "", talker:str = "", delay: float = 0.02, newline: bool = False) -> None: #cColor goes crazy
    #custom color printng function
    if(bool(talker)):
        if(talker.strip().lower() == "developers" or talker.strip().lower() == "developer"):
            printS(BRIGHT_GREEN+BOLD + talker + ": " + Style.RESET_ALL)
        else:
            printS(Fore.BLUE+BOLD + talker + ": " + Style.RESET_ALL)
    print(color, end="", flush=True)
    for i in text:
        try:
            if(i=="["):
                print(Style.RESET_ALL, end="", flush=True)
                print(i, end="", flush=True)
                print(cColor, end="", flush=True)
            elif(i=="]"):
                print(Style.RESET_ALL, end="", flush=True)
                print(i, end="", flush=True)
                print(color, end="", flush=True)
            else:
                print(i, end="", flush=True)
            if not skipping:
                sleep(delay)
                match i:
                    case "\n":
                        sleep(0.4+delay)
                    case ".":
                        sleep(0.2+delay)
                    case ",":
                        sleep(0.1+delay)
                    case _:
                        sleep(delay)    
            if(bool(color)):
                print(Style.RESET_ALL, end="", flush=True)   
            if(newline):
                print() 
        except KeyboardInterrupt:
            delay = 0



## Cool print UI functions that I added for funnies
def printDistort(text: str) -> None:
    nameChars="""†‡@#$%^&*‰\\‰Š~ŒŽ™šœž?¶®""" # wow such creative
    for i in range(len(text)):
        # ah yes I love the ordef of i, _i3, i2 it makes so much sense...
        for _i3 in range(10):
            sleep(0.01)
            var = ""
            # there is literally a random choice thing why are you doing this
            var += nameChars[random.randrange(0,len(nameChars))]
            var += nameChars[random.randrange(0,len(nameChars))]
            var += nameChars[random.randrange(0,len(nameChars))]
            var += nameChars[random.randrange(0,len(nameChars))]
            os.system("clear")
            print(Fore.YELLOW+var,": "+Style.RESET_ALL,end="")
            #for i in range(5):
            #   print(nameChars[random.randint(0,len(nameChars)-1)],end="")
            #print(": ",end="")
            for i2 in range(i-1):
                print(text[i2],flush=True,end="")
    for _ in range(50):

        sleep(0.01)
        var = ""
        var += nameChars[random.randrange(0,len(nameChars))]
        var += nameChars[random.randrange(0,len(nameChars))]
        var += nameChars[random.randrange(0,len(nameChars))]
        var += nameChars[random.randrange(0,len(nameChars))]
        os.system("clear")
        print(Fore.YELLOW+var,": "+Style.RESET_ALL,end="")
        print(text)

def printDecode(text): 
    nameChars="""qwertyuiopasdfghjklzxcvbnm1234567890"""
    ln=len(text)
    for i in range(len(text)+1):
        for j in range(50):
            var =""
            for i in range(len(text)-ln):
                var+=MOTHERSHIP_GREEN+text[i]+Style.RESET_ALL
            for i in range(ln):
                var += nameChars[random.randrange(0,len(nameChars))]

            print(var)
            os.system("clear")


        ln-=1
        os.system("clear")

    print(text)
#

#i held down tab lolpytho
# smh
def getchar(allowed="1234e", prompt=">>> ", strict = False):
    '''gets characters, scans if characters allowed
    paramaters: allowed (characters that can be inputed) prompt (what it asks) 
    strict (whether or not to ask again for empty string)'''
    while True:
        out = input(prompt).strip().lower()
        if strict:
            if out in allowed and out != "":
                return out
            elif out == "": #catchall + redundancy
                return 0
            else:
                printD("Sorry, what was that?","Prism")

        else: 
            if out in allowed:
                return out
            else:
                printD("Sorry, what was that?", "Prism")


def menu(options, flags = []):
    print("Your options are:\n")
    #print(options)
    for i in range(len(options)):
        if("m" in flags and "m" in options[i]):
            print(TAB + "[m]: " + options[i].replace("~m", "")) 
            flags.pop(flags.index("m"))
        elif("t" in flags and "t" in options[i]):
            print(TAB + "[t]: " + options[i].replace("~t", ""))
            flags.pop(flags.index("t"))
        else:
            print(TAB + "[" + str(i+1) + "]: " + options[i])
    print("")
#commented out so i can run code without crashing
#fine i'll test in a different file
#printDistort("This is a string  ")
def OWTVisualizer(map):
    '''Should be a twice-nested list'''
    for x in range(len(map)):
        toPrint=""
        for y in range(len(map[x])):
            toPrint+=map[x][y]+"   "+Style.RESET_ALL
        print(toPrint,"\n")
    return map


## END OF FILE ##