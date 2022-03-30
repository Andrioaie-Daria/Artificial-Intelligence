from Domain.individual import Individual

class Population():
    def __init__(self, populationSize=0, individualSize=0):
        self.__populationSize = populationSize

        self.__individuals = [Individual(individualSize) for x in range(populationSize)]

    def evaluate(self):
        # evaluates the population
        for x in self.__individuals:
            x.computeFitness()

    def selection(self, k=0):
        # RANKING selection
        # perform a selection of k individuals from the population based on each individual's fitness
        # possible alternative: roulette selection 
        sorted_individuals = sorted(self.__individuals, key=lambda individual: individual.getFitness(), reverse=True)
        return sorted_individuals[:k]

    def getIndividuals(self):
        return self.__individuals

    def addIndividual(self, new_individual):
        self.__individuals.append(new_individual)

    def setIndividuals(self, new_individuals):
        self.__individuals.clear()
        self.__individuals.extend(new_individuals)
