class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory):
        self.attack = attack
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.ranged = ranged
        self.necromancy = necromancy
        self.laboratory = laboratory
        self.recipes = {}


class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catelysts = []

    def mixPotion(self):
        pass

    def addReagent(self):
        pass

class Potion:
    def __init__(self, name, stat, boost):
        self.name = name
        self.stat = stat
        self.boost = boost