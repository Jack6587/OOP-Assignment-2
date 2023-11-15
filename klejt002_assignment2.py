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

    def addReagent(self):
        pass

class Potion:
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

    def setBoost(self):
        pass

class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        pass

class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        pass
    
    def getReagent(self):
        pass

    def getPotion(self):
        return self.__potion

class Reagent:
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
        pass

class Herb(Reagent):
    def __init__(self, name, potency, grimy):
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        pass

    def getGrimy(self):
        return self.__grimy
    
    def setGrimy(self):
        pass

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        pass

    def getQuality(self):
        return self.__quality