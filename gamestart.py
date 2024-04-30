import os

from colorama import Fore

from realengine import printS, menu

import pyson

import gameloop

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
input("Resize your window until all of the Xs fit onto one line. \nPress enter to continue once the window is done resizing.\n> ")

os.system("clear")
printS("""
░░░░░██╗░█████╗░░██████╗██╗░░██╗░█████╗░░█████╗░  ░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗███████╗██████╗░
░░░░░██║██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░░░░░██║██║░░██║╚█████╗░███████║██║░░╚═╝██║░░██║  ██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╗░░██║██║░░██║░╚═══██╗██╔══██║██║░░██╗██║░░██║  ██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██████╔╝██║░░██║╚█████╔╝╚█████╔╝  ╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░  ░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""",loader=True)
printS("JoshCo Clicker - Click to Save the World")
printS("Welcome back "+pyson.getData("saves/JOSHCO.pyson","globalusername")) #not actually an error
print("Welcome to JoshCo Clicker. Select your option:")
menu([
    "Load Game"
])
while True:
     match input("$>>> "):
        case "1": #start the game
            print("Starting game...")
            gameloop.mainloop("saves/"+input("Enter save file name: \n> ")+".pyson")
            
        

        case _:
            print("ERROR. Stop fucking with the code smh")

