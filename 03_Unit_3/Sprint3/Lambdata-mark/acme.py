import unittest
import random
from random import randint

class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        s = self.price / self.weight
        if s < 0.5:
            print(f'Not so stealable')
        elif (s >= 0.5) and (s < 1):
            print(f'Kinda stealable.')
        else:
            print(f'Very stealable!')

    def explode(self):
        e = self.flammability * self.weight
        if e < 10:
            print(f'...fizzle.')
        elif (e >= 10) and (e < 50):
            print(f'...boom!')
        else:
            print(f'...BABOOM!!')

class BoxingGlove(Product):
    def __init__(self, name):
        super().__init__(name, weight=10)
    
    def explode(self):
        print(f"it's a glove.")
    
    def punch(self):
        if self.weight < 5:
            print(f'That tickles')
        elif 5 <= self.weight < 15:
            print('Hey that hurt!')
        else:
            print('OUCH!')