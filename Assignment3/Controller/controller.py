from Domain.Drone import Drone
from Domain.map import Map


class Controller():
    def __init__(self, repository):
        self.__repository = repository
        self.__map = Map()
        self.__map.randomMap()
        # self.__map.loadMap("test1.map")

        # we position the drone somewhere in the area
        [x, y] = self.__map.getRandomEmptySquare()
        # create drone
        self.__drone = Drone(x, y)
    
    def iteration(self):
        # QUESTION:
        # do we only select 2 random parents for each iteration or use the function selection() from the class Population,
        # which selects based on the fitness level of the individuals?

        # do we select only  2 parents or more?

        #TODO a iteration:
        # selection of the parents
        # create offsprings by crossover of the parents
        # apply some mutations on the offsprings
        # selection of the survivors
        statistics = []

        return statistics
        
    def run(self):
        # args - list of parameters needed in order to run the algorithm
        # TODO implement
        # until stop condition
        #    perform an iteration
        #    save the information need it for the statistics
        statistics = []

        random_seed = 1
        while random_seed <= 30:
            statistics = self.iteration()
            random_seed += 1

        # return the results and the info for statistics
        return statistics
    
    def solver(self, population_size, battery_life):
        #TODO implement
        # create the population,
        # run the algorithm
        # return the results and the statistics
        self.__repository.createPopulation(population_size, battery_life)
        statistics = self.run()
        return statistics

    def getMap(self):
        return self.__map

    def setMap(self, new_map):
        self.__map = new_map
