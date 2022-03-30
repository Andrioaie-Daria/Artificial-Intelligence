# -*- coding: utf-8 -*-

from Domain.population import *
from Domain.map import Map

class Repository():
    def __init__(self):
        # QUESTION: do we really need a list of populations? doesn't the algorithm run the 30 iterations on the same population?
        self.__populations = []
        self.map = Map()
        
    def createPopulation(self, population_size, individual_size):
        return Population(population_size, individual_size)

    def getPopulations(self):
        return self.__populations


    #TODO : add the other components for the repository:
    #    load and save from file, etc
            