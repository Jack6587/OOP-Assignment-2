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
        self.__laboratory.mixPotion(recipe, type, stat, primaryIngredient, secondaryIngredient)


    def drinkPotion(self, potion):
        """Here the alchemist drinks a potion provided by the user. Based on the potion they drink, their attributes can increase"""
        statType = potion.getStat()
        boost = potion.calculateBoost()
        
        if statType == "attack":
            self.__attack += boost
            return f"My attack has been increased by {boost}!"
        if statType == "strength":
            self.__strength += boost
            return f"My strength has been increased by {boost}!"
        if statType == "defence":
            self.__defence += boost
            return f"My defence has been increased by {boost}!"
        if statType == "magic":
            self.__magic += boost
            return f"My magic has been increased by {boost}!"
        if statType == "ranged":
            self.__ranged += boost
            return f"My magic has increased by {boost}!"
        if potion.getStat() == "necromancy":
            self.__necromancy += boost
            return f"My necromancy has increased by {boost}!"

    def collectReagent(self, reagent, amount):
        self.__laboratory.addReagent(reagent, amount)

    def refineReagents(self):
        for potion in self.__laboratory._Laboratory__potions:
            for herb in potion.herbs:
                herb.refine()
            for catalyst in potion.catalysts:
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
        """This function creates a potion based on the parameters and a provided first and second ingredient. It validates that the ingredients exist and are available.
        It takes a name, type (of potion), a stat, and two ingredients based on the assignment specs. Both ingredients are initialised as none, to hold the actual ingredient type.
        Then, we have two for loops. The first iterates over "herbName" and herb, where the primaryIngredient variable is assigned to herb if it correlates with the input.
        The next for loop does the same thing, but checks to see if the primaryIngredient variable has already been found. Next, we check if the potion is a Super Potion.
        If it is, we check for catalyst as the second ingredient. If they are equal to each other, the secondIngredient variable becomes a catalyst.
        Then, we create the SuperPotion instance if both ingredients have been found, adding it to the list of potions. Output correlates with the outcome.
        Alternatively, the type could be an ExtremePotion. If this is the case, we want the secondaryIngredient to be a SuperPotion. The same steps are taken to create an ExtremePotion.
        """
        primaryIngredientObject = None
        secondaryIngredientObject = None

        for herbName, herb in self.__herbs:
            if herbName == primaryIngredient:
                primaryIngredientObject = herb

        if primaryIngredientObject is None:
            for catalystName, catalyst in self.__catalysts:
                if catalystName == primaryIngredient:
                    primaryIngredientObject = catalyst

        if type == 'SuperPotion':
            for catalystName, catalyst in self.__catalysts:
                if catalystName == secondaryIngredient:
                    secondaryIngredientObject = catalyst
            if primaryIngredientObject and secondaryIngredientObject:
                newPotion = SuperPotion(name, stat, 0, primaryIngredientObject, secondaryIngredientObject)
                self.__potions.append(newPotion)
                print(f"*Subtle bubbling*... The Super {stat} potion finished brewing!")

        elif type == 'ExtremePotion':
            for potion in self.__potions:
                if potion.getName() == secondaryIngredient:
                    secondaryIngredientObject = potion
            if primaryIngredientObject and secondaryIngredientObject:
                newPotion = ExtremePotion(name, stat, 0, primaryIngredientObject, secondaryIngredientObject)
                self.__potions.append(newPotion)
                print(f"*Intense bubbling*... Boom, the Extreme {stat} potion almost exploded!")

    def addReagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            self.__herbs.append((reagent.getName(), reagent))
        elif isinstance(reagent, Catalyst):
            self.__catalysts.append((reagent.getName(), reagent))


class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = None

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
    boost = property(getBoost, setBoost)


class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst
        self.setBoost(round(herb.getPotency() + (catalyst.getPotency() * catalyst.getQuality()) * 1.5, 2))

    def calculateBoost(self):
        return self.getBoost()

    def getHerb(self):
        return self.__herb
    
    def getCatalyst(self):
        return self.__catalyst


class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion
        self.setBoost(round((reagent.getPotency() * potion.getBoost()) * 3.0, 2))


    def calculateBoost(self):
        return self.getBoost()

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
        self._Herb__potency = potency
        self.__grimy = True

    def refine(self):
        if self.__grimy:
            self.__potency *= 2.5
            self.__grimy = False

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
for potion in alchemist.laboratory._Laboratory__potions:
    print(f"\n{potion.name} Boost:", potion.boost)
    alchemist.drinkPotion(potion)