from random import *

class Gene:
    # each gene has an integer code in the range [0,3], symbolising the direction of each step
    # UP = 0, DOWN = 2, LEFT = 1, RIGHT = 3
    def __init__(self):
        # random initialise the gene according to the representation
        self.__code = randint(0, 3)

    def setGene(self, code):
        self.__code = code

    def getCode(self):
        return self.__code
