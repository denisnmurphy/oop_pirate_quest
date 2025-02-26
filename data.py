from pirates import Captain, Quartermaster, Officer, CannonOperator, Cook, DeckScrubber
import json

class DataLoader:
    def load_pirates(self):
        return [
        Captain("Harry"),
        Quartermaster("Isabel"),
        Officer("BootStrap Bill"),
        CannonOperator("Powder Joe"),
        Officer("Four Finger Fritz"),
        CannonOperator("Lady Joyce"),
        Officer("Calypso"),
        CannonOperator("Moustache Mike")
        ]

print(DataLoader.load_pirates)

class JSONDataloader:
    def load_pirates(self):
        with open("data.json") as file:
            data = json.load(file)
        pirates = []
        for pirate in data["pirates"]:
            if pirate["title"] == "Captain":
                pirates.append(Captain(pirate["name"]))
            elif pirate["title"] == "Quartermaster":
                    pirates.append(Quartermaster(pirate["name"]))
            elif pirate["title"] == "Officer":
                pirates.append(Officer(pirate["name"]))
            elif pirate["title"] == "Cannon Operator":
                pirates.append(CannonOperator(pirate["name"]))
            elif pirate["title"] == "Cook":
                pirates.append(Cook(pirate["name"]))
            elif pirate["title"] == "Deck Scrubber":
                pirates.append(DeckScrubber(pirate["name"]))
        return pirates
