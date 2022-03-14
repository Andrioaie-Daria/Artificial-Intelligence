import pickle, pygame
from random import random, randint
import numpy as np

#Creating some colors
BLUE  = (0, 0, 255)
GRAYBLUE = (50,120,120)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#define directions
UP = 0
DOWN = 2
LEFT = 1
RIGHT = 3

class Environment():
    def __init__(self):
        self.__n = 20
        self.__m = 20
        self.__surface = np.zeros((self.__n, self.__m))
        self.randomMap()

    def randomMap(self, fill=0.2):
        for i in range(self.__n):
            for j in range(self.__m):
                if random() <= fill:
                    self.__surface[i][j] = 1

    def __str__(self):
        string = ""
        for i in range(self.__n):
            for j in range(self.__m):
                string = string + str(int(self.__surface[i][j]))
            string = string + "\n"
        return string

    def readUDMSensors(self, x, y):
        readings = [0, 0, 0, 0]
        # UP
        current_x = x - 1
        while (current_x >= 0) and (self.__surface[current_x][y] == 0):
            current_x = current_x - 1
            readings[UP] = readings[UP] + 1
        # DOWN
        current_x = x + 1
        while (current_x < self.__n) and (self.__surface[current_x][y] == 0):
            current_x = current_x + 1
            readings[DOWN] = readings[DOWN] + 1
        # LEFT
        current_y = y + 1
        while (current_y < self.__m) and (self.__surface[x][current_y] == 0):
            current_y = current_y + 1
            readings[LEFT] = readings[LEFT] + 1
        # RIGHT
        current_y = y - 1
        while (current_y >= 0) and (self.__surface[x][current_y] == 0):
            current_y = current_y - 1
            readings[RIGHT] = readings[RIGHT] + 1

        return readings

    def saveEnvironment(self, numFile):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def loadEnvironment(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.__n = dummy.__n
            self.__m = dummy.__m
            self.__surface = dummy.__surface
            f.close()

    def image(self, colour=BLUE, background=WHITE):
        imagine = pygame.Surface((420, 420))
        brick = pygame.Surface((20, 20))
        brick.fill(BLUE)
        imagine.fill(WHITE)
        for i in range(self.__n):
            for j in range(self.__m):
                if (self.__surface[i][j] == 1):
                    imagine.blit(brick, (j * 20, i * 20))

        return imagine

    def getRandomEmptySquare(self):
        x = randint(0, self.__n - 1)
        y = randint(0, self.__m - 1)
        while self.__surface[x][y] == 1:
            x = randint(0, self.__n - 1)
            y = randint(0, self.__m - 1)
        return [x, y]
