'''
File: klejt002_assignment.py
Description: This Python module reflects the functions of an RPG game. The main focus is that of an alchemist that belongs to a laboratory, who can mix and drink potions.
Author: Jack Klenke
StudentID: 110349473
EmailID: klejt002
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod

class Alchemist:
    def __init__(self, attack, strength, defence, magic, ranged, necromancy):
        if not all(0 <= stat <= 100 for stat in [attack, strength, defence, magic, ranged, necromancy]):
            raise ValueError("All stats must be between 0 and 100.")
        
        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        
        self.__laboratory = Laboratory()
        self.__recipes = {
            "Super Attack": ("Irit", "Eye of Newt"),
            "Super Strength": ("Kwuarm", "Limpwurt Root"),
            "Super Defence": ("Cadantine", "White Berries"),
            "Super Magic": ("Lantadyme", "Potato Cactus"),
            "Super Ranging": ("Dwarf Weed", "Wine of Zamorak"),
            "Super Necromancy": ("Arbuck", "Blood of Orcus"),
            "Extreme Attack": ("Avantoe", "Super Attack"),
            "Extreme Strength": ("Dwarf Weed", "Super Strength"),
            "Extreme Defence": ("Lantadyme", "Super Defence"),
            "Extreme Magic": ("Ground Mud Rune", "Super Magic"),
            "Extreme Ranging": ("Grenwall Spike", "Super Ranging"),
            "Extreme Necromancy": ("Ground Miasma Rune", "Super Necromancy"),
        }

    def getLaboratory(self):
        return self.__laboratory
    
    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe):
        if recipe in self.__recipes:
            primaryIngredient, secondaryIngredient = self.__recipes[recipe]
            potion = self.__laboratory.mixPotion(recipe, primaryIngredient, secondaryIngredient)
            return potion

    def drinkPotion(self, potion):
        if potion.getStat() == "attack":
            self.__attack = min(self.__attack + potion.getBoost(), 100)
        if potion.getStat() == "strength":
            self.__strength = min(self.__strength + potion.getBoost(), 100)
        if potion.getStat() == "defence":
            self.__defence = min(self.__defence + potion.getBoost(), 100)
        if potion.getStat() == "magic":
            self.__magic = min(self.__magic + potion.getBoost(), 100)
        if potion.getStat() == "ranged":
            self.__ranged = min(self.__ranged + potion.getBoost(), 100)
        if potion.getStat() == "necromancy":
            self.__necromancy = min(self.__necromancy + potion.getBoost(), 100)

    def collectReagent(self, reagent, amount):
        self.__laboratory.addReagent(reagent, amount)

    def refineReagents(self):
        self.__laboratory.cleanHerbs()
        self.__laboratory.refineCatalysts()


class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        for herb, amount in self.__herbs:
            if herb.getName() == primaryIngredient and amount > 0:
                primIngredient = herb
        for catalyst, amount in self.__catalysts:
            if catalyst.getName() == primaryIngredient and amount > 0:
                primIngredient = catalyst

        for catalyst, amount in self.__catalysts:
            if catalyst.getName() == secondaryIngredient and amount > 0:
                secIngredient = catalyst

    def addReagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            self.__herbs.append((reagent, amount))
        elif isinstance(reagent, Catalyst):
            self.__catalysts.append((reagent, amount))

    def grabReagent(self, name):
        for herb, amount in self.__herbs:
            if herb.getName() == name:
                return herb, amount
            
        for catalyst, amount in self.__catalysts:
            if catalyst.getName() == name:
                return catalyst, amount

    def cleanHerbs(self):
        for h in range(len(self.__herbs)):
            herb, amount = self.__herbs[h]
            herb.refine()

    def refineCatalysts(self):
        for c in range(len(self.__catalysts)):
            catalyst, amount = self.__catalyst[c]
            catalyst.refine()

class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name

    def getStat(self):
        return self.__stat
    
    def getBoost(self):
        return self.__boost

    def setBoost(self, boost):
        self.__boost = boost


class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        self.__boost = self.__herb.getPotency() + (self.__catalyst.getPotency() * self.__catalyst.getQuality()) * 1.5

    def getHerb(self):
        return self.__herb
    
    def getCatalyst(self):
        return self.__catalyst


class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, superPotion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__superPotion = superPotion

    def calculateBoost(self):
        self.__boost = ((self.__reagent.getPotency() * self.__superPotion.getBoost()) * 3.0)
    
    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion


class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency
    
    def setPotency(self, potency):
        self.__potency = potency


class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):
        if self.__grimy:
            self.__potency *= 2.5
            self.__grimy = False
            print("{self.getName()} herb has been refined.")

    def getGrimy(self):
        return self.__grimy
    
    def setGrimy(self, grimy):
        self.__grimy = grimy


class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print("{self.getName()} catalyst quality has been increased to {self.getQuality()}.")
        elif self.__quality >= 8.9:
            self.__quality = 10
            print("{self.getName()} catalyst has been refined to max quality.")


    def getQuality(self):
        return self.__quality
