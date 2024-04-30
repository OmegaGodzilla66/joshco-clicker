import pyson
import realengine as real

import saves

class Game:
    def __init__(self, save_path):
        "Initialze the game"
        # Initiate the game vars
        self.save_path=save_path # for resaving data
        self.clicks=pyson.getData(save_path,"clicks")
        self.user=pyson.getData(save_path,"localUser")
        self.upgrades=pyson.getData(save_path,"boughtShop")
        self.clicksPerTick=pyson.getData(save_path,"clicksPerTick")
        self.clicksPerClick=pyson.getData(save_path,"clicksPerClick")

    def save(self):
        "Saves the game, DOESN'T WORK RN"
        
        real.printD("FIX THIS","Developers")

    def click(self):
        "Click"
        self.clicks+=self.clicksPerClick


def mainloop(path):
    """Main loop that the game occures in
    At least it's better than that infinate recursion bs that OWT doese smh"""
    game=Game(path)
    while True:
        real.clear()
        print(f"You have {game.clicks} clicks")
        input("> ")
        game.click()

        # Save at the end
        game.save()