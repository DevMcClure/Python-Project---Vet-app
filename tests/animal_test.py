import unittest
from models.animal import Animal

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("Toffie", "Phil Mitchell", "07.11.16", "Dog", "06912738109", "Bestest Doggo", True)



    def test_animal_has_name(self):
        self.assertEqual("Toffie", self.animal.animal_name)    