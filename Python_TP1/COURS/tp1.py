import math
from random import randint
from random import random

def Sphere(x,y):
    return x**2 + y**2

def trad(x):
    return (x-0.5)*2*5

print(Sphere(trad(1),trad(1)))

class Cell:
    def __init__(self, genome):
        self.genome = genome

    def child(self):
        new_genome = Cell(self.genome)
        new_genome.genome[randint(0,len(self.genome)-1)] = random()

    def apply(self):
        trad(self.genome)

    #def reset(self):





