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
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory):
        self.__attack = max(0, min(attack, 100))
        self.__strength = max(0, min(strength, 100))
        self.__defense = max(0, min(defense, 100))
        self.__magic = max(0, min(magic, 100))
        self.__ranged = max(0, min(ranged, 100))
        self.__necromancy = max(0, min(necromancy, 100))

        self.__laboratory = laboratory
        self.__recipes = {}

    def getLaboratory(self):
        return self.__laboratory
    
    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe):
        pass

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagents(self):
        pass


class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

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
        pass

    def refineCatalysts(self):
        pass

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
    def __init__(self, name, potency, grimy):
        super().__init__(name, potency)
        self.__grimy = grimy

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