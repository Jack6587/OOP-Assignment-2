import unittest
from klejt002_assignment2 import *

import unittest

class TestAlchemist(unittest.TestCase):
    def testInvalidStatInitialisation(self):
        with self.assertRaises(ValueError):
            Alchemist(101, 50, 50, 50, 50, 50)

    

unittest.main()