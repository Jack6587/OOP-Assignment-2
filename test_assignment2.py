import unittest
from klejt002_assignment2 import *


class TestAlchemist(unittest.TestCase):
    def setUp(self):
        self.alchemist = Alchemist(100, 30, 40, 70, 50, 40)
        herb = self.alchemist.collectReagent(Herb("Irit", 1.0), 1)
        catalyst = self.alchemist.collectReagent(Catalyst("Eye of Newt", 4.3, 1.0), 1)

    def testInvalidInitialisation(self):
        with self.assertRaises(ValueError):
            Alchemist(101, 40, 50, 50, 50, 50)

    def testPotionMixing(self):
        self.alchemist.mixPotion("Super Attack")
        self.assertEqual(len(self.alchemist.laboratory.potions), 1)

    def testIncorrectPotionMixing(self):
        with self.assertRaises(KeyError):
            self.alchemist.mixPotion("Recipe not recognised")


class TestPotion(unittest.TestCase):
    alchemist = Alchemist(100, 30, 40, 70, 50, 40)
    herb = alchemist.collectReagent(Herb("Lantadyme", 2.0), 1)
    superCatalyst = alchemist.collectReagent(Catalyst("Potato Cactus", 7.3, 0.1), 1)
    extremeCatalyst = alchemist.collectReagent(Catalyst("Ground Mud Rune", 2.1, 6.7), 1)
    alchemist.mixPotion("Super Magic")
    alchemist.mixPotion("Extreme Magic")

    def testCalculateBoostSuperPotion(self):
        superMagic = self.alchemist.laboratory.potions[0]
        self.assertAlmostEqual(superMagic.boost, 3.095)

    def testCalculateBoostExtremePotion(self):
        extremeMagic = self.alchemist.laboratory.potions[1]
        self.assertAlmostEqual(extremeMagic.boost, 19.4985)

class TestReagent(unittest.TestCase):
    

unittest.main()