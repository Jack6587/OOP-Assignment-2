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
            'Super Attack': ('SuperPotion', 'Attack', 'Irit', 'Eye of Newt'),
            'Super Strength': ('SuperPotion', 'Strength', 'Kwuarm', 'Limpwurt Root'),
            'Super Defence': ('SuperPotion', 'Defence', 'Cadantine', 'White Berries'),
            'Super Magic': ('SuperPotion', 'Magic', 'Lantadyme', 'Potato Cactus'),
            'Super Ranging': ('SuperPotion', 'Ranged', 'Dwarf Weed', 'Wine of Zamorak'),
            'Super Necromancy': ('SuperPotion', 'Necromancy', 'Arbuck', 'Blood of Orcus'),
            'Extreme Attack': ('ExtremePotion', 'Attack', 'Avantoe', 'Super Attack'),
            'Extreme Strength': ('ExtremePotion', 'Strength', 'Dwarf Weed', 'Super Strength'),
            'Extreme Defence': ('ExtremePotion', 'Defence', 'Lantadyme', 'Super Defence'),
            'Extreme Magic': ('ExtremePotion', 'Magic', 'Ground Mud Rune', 'Super Magic'),
            'Extreme Ranging': ('ExtremePotion', 'Ranged', 'Grenwall Spike', 'Super Ranging'),
            'Extreme Necromancy': ('ExtremePotion', 'Necromancy', 'Ground Miasma Rune', 'Super Necromancy'),
        }


    def getLaboratory(self):
        return self.__laboratory
    
    laboratory = property(getLaboratory)
    
    def getRecipes(self):
        return self.__recipes
    
    recipes = property(getRecipes)

    def mixPotion(self, recipe):
        """Mixes a potion for a provided recipe name. This utilise the laboratory function mixPotion"""
        type, stat, primaryIngredient, secondaryIngredient = self.__recipes[recipe]
        self.laboratory.mixPotion(recipe, type, stat, primaryIngredient, secondaryIngredient)


    def drinkPotion(self, potion):
        """Here the alchemist drinks a potion provided by the user. Based on the potion they drink, their attributes can increase, utilising the boost and stat properties"""
        statType = potion.stat
        
        if statType == "Super Attack":
            self.__attack += potion.boost
        if statType == "Super Strength":
            self.__strength += potion.boost
        if statType == "Super Defence":
            self.__defence += potion.boost
        if statType == "Super Magic":
            self.__magic += potion.boost
        if statType == "Super Ranged":
            self.__ranged += potion.boost
        if statType == "Super Necromancy":
            self.__necromancy += potion.boost
        elif potion.stat == "Extreme Attack":
            self.__attack += potion.boost
        elif potion.stat == "Extreme Strength":
            self.__strength += potion.boost
        elif potion.stat == "Extreme Defense":
            self.__defense += potion.boost
        elif potion.stat == "Extreme Magic":
            self.__magic += potion.boost
        elif potion.stat == "Extreme Ranging":
            self.__ranged += potion.boost
        elif potion.stat == "Extreme Necromancy":
            self.__necromancy += potion.boost

    def collectReagent(self, reagent, amount):
        """Collects and adds reagent to laboratory's catalyst/herb list"""
        self.__laboratory.addReagent(reagent, amount)

    def refineReagents(self):
        """Utilises each reagent's individual refine method (such as changing potency/quality). It does so for every herb and catalyst in the laboratory"""
        for herb in self.laboratory.herbs:
            herb.refine()
        for catalyst in self.laboratory.catalysts:
            catalyst.refine()


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

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        """This function creates a potion based on ingredients. It checks to make sure that the primaryIngredient is herb and if the input is a SuperPotion, initialises catalyst as the secondaryIngredient. If it hasn't found a primaryIngredient, it performs a similar operation yet catalyst is assigned the first ingredient and SuperPotion the second. caculateBoost is performed before added to the potions list"""
        primaryIngredientObject = None
        secondaryIngredientObject = None

        for herb in self.herbs:
            if herb.name == primaryIngredient:
                primaryIngredientObject = herb

        if type == "SuperPotion":
            for catalyst in self.catalysts:
                if catalyst.name == secondaryIngredient:
                    secondaryIngredientObject = catalyst

                newPotion = SuperPotion(name, stat, primaryIngredientObject, secondaryIngredientObject)
                print(f"*Subtle bubbling*... The Super {stat} potion finished brewing!")

        if primaryIngredientObject == None:
            for catalyst in self.catalysts:
                if catalyst.name == primaryIngredient:
                    primaryIngredientObject = catalyst

        if type == "ExtremePotion":
            for potion in self.__potions:
                if potion.name == secondaryIngredient:
                    secondaryIngredientObject = potion

                newPotion = ExtremePotion(name, stat, primaryIngredientObject, secondaryIngredientObject)
                print(f"*Intense bubbling*... Boom, the Extreme {stat} potion almost exploded!")

        newPotion.calculateBoost()

        self.potions.append(newPotion)


    def addReagent(self, reagent, amount):
        """Adds a specific amount of a type of reagent to the laboratorty's herbs list """
        while amount > 0:
            if isinstance(reagent, Herb):
                self.herbs.append(reagent)
            elif isinstance(reagent, Catalyst):
                self.catalysts.append(reagent)
            amount = amount - 1

    def getPotions(self):
        return self.__potions
    
    def getHerbs(self):
        return self.__herbs
    
    def getCatalysts(self):
        return self.__catalysts
    
    potions = property(getPotions)
    herbs = property(getHerbs)
    catalysts = property(getCatalysts)


class Potion(ABC):
    def __init__(self, name, stat):
        self.__name = name
        self.__stat = stat
        self.__boost = 0

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

    name = property(getName)
    stat = property(getStat)
    boost = property(getBoost, setBoost)


class SuperPotion(Potion):
    def __init__(self, name, stat, herb, catalyst):
        super().__init__(name, stat)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        self.boost = self.herb.potency + (self.catalyst.potency * self.catalyst.quality) * 1.5

    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst
    
    herb = property(getHerb)
    catalyst = property(getCatalyst)


class ExtremePotion(Potion):
    def __init__(self, name, stat, reagent, potion):
        super().__init__(name, stat)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        self.boost = (self.reagent.potency * self.potion.boost) * 3.0

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion
    
    reagent = property(getReagent)
    potion = property(getPotion)


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

    name = property(getName)
    potency = property(getPotency, setPotency)


class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):
        if self.__grimy:
            self.potency *= 2.5
            self.grimy = False

    def getGrimy(self):
        return self.__grimy
    
    def setGrimy(self, grimy):
        self.__grimy = grimy

    grimy = property(getGrimy, setGrimy)


class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
        elif self.__quality >= 8.9:
            self.__quality = 10

    def getQuality(self):
        return self.__quality
    
    quality = property(getQuality)

alchemist = Alchemist(72, 35, 92, 66, 99, 100)

alchemist.collectReagent(Herb("Irit", 1.0), 1)
alchemist.collectReagent(Herb("Kwuarm",1.2), 1)
alchemist.collectReagent(Herb("Cadantine", 1.5), 1)
alchemist.collectReagent(Herb("Lantadyme", 2.0), 1)
alchemist.collectReagent(Herb("Dwarf Weed", 2.5), 1)
alchemist.collectReagent(Herb("Arbuck", 2.6), 1)
alchemist.collectReagent(Herb("Avantoe", 3.0), 1)
alchemist.collectReagent(Herb("Torstol", 4.5), 1)

alchemist.collectReagent(Catalyst("Eye of Newt", 4.3, 1.0), 1)
alchemist.collectReagent(Catalyst("Limpwurt Root", 3.6, 1.7), 1)
alchemist.collectReagent(Catalyst("White Berries", 1.2, 2.0), 1)
alchemist.collectReagent(Catalyst("Potato Cactus", 7.3, 0.1), 1)
alchemist.collectReagent(Catalyst("Wine of Zamorak", 1.7, 5.0), 1)
alchemist.collectReagent(Catalyst("Blood of Orcus", 4.5, 2.2), 1)
alchemist.collectReagent(Catalyst("Ground Mud Rune", 2.1, 6.7), 1)
alchemist.collectReagent(Catalyst("Grenwall Spike", 6.3, 4.9), 1)
alchemist.collectReagent(Catalyst("Ground Miasma Rune",3.3, 5.2), 1)

alchemist.refineReagents()

print("-" * 40 + "Mix Potions from Recipes" + "-" * 40)
for recipe in alchemist.recipes:
    alchemist.mixPotion(recipe) 

print("-" * 40 + "Drink Potions" + "-" * 40)
for potion in alchemist.laboratory.potions:
    print(f"\n{potion.name} Boost:", potion.boost)
    alchemist.drinkPotion(potion)