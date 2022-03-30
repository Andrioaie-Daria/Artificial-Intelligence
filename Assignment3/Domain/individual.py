from Domain.gene import Gene
from random import *

class Individual:
    # a possible solution
    def __init__(self, size=0):
        self.__size = size
        self.__chromosome = [Gene() for i in range(self.__size)]
        self.__fitness = None

    def computeFitness(self):
        # count the green cells
        # whenever it bumps into a wall or edge, it simply stops until there is a valid move 
        #save it in self.__fitness
        pass

    def setChromosome(self, new_chromosome):
        self.__chromosome = new_chromosome
        self.__size = len(new_chromosome)

    def getFitness(self):
        return self.__fitness

    def getGeneByIndex(self, index):
        return self.__chromosome[index]

    def mutate(self, mutateProbability=0.04):
        # random resetting for every gene

        for gene in self.__chromosome:
            if random() < mutateProbability:
                gene.setGene(randint(0, 3))

        return self

    def crossover(self, otherParent, crossoverProbability=0.8):
        # Uniform crossover

        offspring1, offspring2 = Individual(), Individual()
        chromosome1 = []
        chromosome2 = []

        for gene_index in range(self.__size):
            if random() < crossoverProbability:
                chromosome1.append(self.getGeneByIndex(gene_index))
                chromosome2.append(otherParent.getGeneByIndex(gene_index))
            else:
                chromosome1.append(otherParent.getGeneByIndex(gene_index))
                chromosome2.append(self.getGeneByIndex(gene_index))

        offspring1.setChromosome(chromosome1)
        offspring2.setChromosome(chromosome2)
        return offspring1, offspring2
