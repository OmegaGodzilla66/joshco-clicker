import realengine as real
import pyson_data as pyson

class MainShop:
    def __init__(self):
        self.clickUpgrades=["+5 clicks per click","x2 clicks per click"]
        self.clickUpgradesCosts=[10,100]



def mainshop(game):
    real.printD("Welcome to the shop! Here you can buy different upgrades")
    real.printD("If by different you mean the exact same upgrade","Developers")
    real.printD("Shut up","OmegaGodzilla66")
    global defaultUpgrades
    real.menu(["Click Upgrades"])
    match input("\n> "):
        case "1":
            real.menu(["+5 clicks per click","x2 clicks per click"])
            match real.getchar("12"):
                case "1":
                    game.clicks-=10
                    game.clicksPerClick+=5
                    game.save()
                case "2":
                    print("E")

        case _:
            raise Exception("SOFTWARE ERROR: ")