import pyson_data as pyson
import realengine as real

import shop

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
        
        pyson.updateData(self.save_path, "clicks",str(self.clicks))
        pyson.updateData(self.save_path, "clicksPerTick", self.clicksPerTick)
        pyson.updateData(self.save_path, "clicksPerClick", self.clicksPerClick)
        # Temp solution while I test

    def click(self):
        "Click"
        self.clicks+=self.clicksPerClick # NOT AN ERROR


def mainloop(path):
    """Main loop that the game occures in
    At least it's better than that infinate recursion bs that OWT doese smh"""
    game=Game(path)
    while True:
        real.clear()
        mr=real.menu(["Click!","Shop"])
        match real.getchar("12"):
            case "1":
                clickloop(game)

            case "2":
                shop.mainshop(game)
            case _:
                raise Exception("SOFTWARE ERROR\nMatch loop in gameloop/mainloop does not match real.menu input.")

        # Save at the end
        game.save()

def clickloop(game):
    """Click loop"""
    while True:
        real.clear()
        print(f"You have {game.clicks} clicks")
        if input("> ").lower() == "exit": return
        game.click()

        # Save at the end
        game.save()