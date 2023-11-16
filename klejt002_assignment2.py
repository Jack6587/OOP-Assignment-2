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
    """
    A class that represents the "Alchemist"

    Attributes
    ---------
    All int attributes must be between 0 and 100.
    attack : int
        number that represents the alchemist's attack power
    strength : int
        number that represents the alchemist's strength level. 
    defence : int
        number that represents the alchemist's defence stats.
    magic : int
        number that represents the alchemist's magic ability.
    ranged : int
        number that represents the alchemisst's ranged capabilities.
    laboratory : (Laboratory)
        This references the laboratory class, that is owned by the alchemist.
    recipes : dictionary
        This is a collection of recipes of different potions that the alchemist knows and can use.
    """
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
        """Mixes a potion for a provided recipe name. This utilise the laboratory function mixPotion"""
        if recipe in self.__recipes:
            primaryIngredient, secondaryIngredient = self.__recipes[recipe]
            potion = self.__laboratory.mixPotion(recipe, primaryIngredient, secondaryIngredient)
            return potion

    def drinkPotion(self, potion):
        """Here the alchemist drinks a potion provided by the user. Based on the potion they drink, their attributes can increase"""
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
        """Adds an "amount" of a certain reagent to the laboratory. Use of the function addReagent here. Takes reagent and amount as parameters"""
        self.__laboratory.addReagent(reagent, amount)

    def refineReagents(self):
        """Refines both herbs and catalysts using functions from the Catalyst and Herb classes. Refining increases the quality"""
        self.__laboratory.cleanHerbs()
        self.__laboratory.refineCatalysts()


class Laboratory:
    """
    A class that represents the alchemist's laboratory, as shown in the initialisation of the Alchemist class

    Attributes
    ----------

    Laboratory does not take any parameters as input but initialises 3 lists:

    self.__potions : list
        Stores all the potions that are created from mixPotions function
    self.__herbs : list
        Stores all herbs added to the laboratory through addReagent
    self.__catalysts : list
        Stores all catalysts added to the laboratory, similar to the herbs
    """
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, potionType, stat, namePrimaryIngredient, nameSecondaryIngredient):
        """This function creates a potion based on the parameters and a provided first and second ingredient. It validates that the ingredients exist and are available.
        It takes a name, type (of potion), a stat, and two ingredients based on the assignment specs
        
        """
        primaryIngredient = self.grabReagent(namePrimaryIngredient)[0]
        secondaryIngredient = self.grabReagent(nameSecondaryIngredient)[0]

        if not primaryIngredient or not secondaryIngredient:
            print("An ingredient or two is missing")
            return None
        
        potion = None

        if potionType == "SuperPotion":
            potion = SuperPotion(name, stat, 0, primaryIngredient, secondaryIngredient)
        elif potionType == "ExtremePotion":
            potion = ExtremePotion(name, stat, 0, primaryIngredient, secondaryIngredient)

        if potion:
            potion.calculateBoost()
            self.__potions.append(potion)
            return potion
        else:
            print("Could not create potion")
            return None

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
            catalyst, amount = self.__catalysts[c]
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
        self.setBoost(round(self.__herb.getPotency() + (self.__catalyst.getPotency() * self.__catalyst.getQuality()) * 1.5, 2))

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
        self.setBoost(round((self.__reagent.getPotency() * self.__superPotion.getBoost()) * 3.0, 2))
    
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
            print(f"{self.getName()} herb has been refined.")

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
            print(f"{self.getName()} catalyst quality has been increased to {self.getQuality()}.")
        elif self.__quality >= 8.9:
            self.__quality = 10
            print(f"{self.getName()} catalyst has been refined to max quality.")

    def getQuality(self):
        return self.__quality
