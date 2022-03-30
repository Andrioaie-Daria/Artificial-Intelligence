import pickle
from random import *
import numpy as np

class Map():
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

    def randomMap(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill:
                    self.surface[i][j] = 1

    def getSurface(self):
        return self.surface

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string

    def loadMap(self, map_file):
        # with open(map_file, "rb") as input_file:
        #     dummy = pickle.load(input_file)
        #     self.n = dummy.n
        #     self.m = dummy.m
        #     self.surface = dummy.surface

        # for some reason, this function throws an error
        pass

    def saveMap(self, filename="test.map"):
        with open(filename, 'wb') as output_file:
            pickle.dump(self, output_file)

    def getRandomEmptySquare(self):
        x = randint(0, self.n - 1)
        y = randint(0, self.m - 1)
        while self.surface[x][y] == 1:
            x = randint(0, self.n - 1)
            y = randint(0, self.m - 1)
        return [x, y]
