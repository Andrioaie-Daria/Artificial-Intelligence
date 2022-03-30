# -*- coding: utf-8 -*-
# imports

# create a menu
#   1. map options:
#         a. create random map
#         b. load a map
#         c. save a map
#         d visualise map
#   2. EA options:
#         a. parameters setup
#         b. run the solver
#         c. visualise the statistics
#         d. view the drone moving on a path
#              function gui.movingDrone(currentMap, path, speed, markseen)
#              ATENTION! the function doesn't check if the path passes trough walls
from Domain.individual import Individual
from Domain.map import Map
from UI.gui import GUI


class UI:
    def __init__(self, controller):
        self.__controller = controller
        self.population_size = 50
        self.individual_size = 10
        self.number_of_generations = 20
        self.number_of_iterations = 100
        self.best_individual = Individual()

    def printMenu(self):
        print("1: Map options")
        print("2: EA options")
        print("0: Exit")


    def printMapMenu(self):
        print("1: Generate random map")
        print("2: Load map from file")
        print("3: Save map to file")
        print("4: See map")
        print("0: Exit")


    def printEAMenu(self):
        print("1: Set parameters")
        print("2: Run the solver")
        print("0: Exit")

        #TODO make thise available only after running the solver
        print("3: View drone on a path")


    def runMapOptions(self):
        new_map = Map()

        while True:
            self.printMapMenu()
            option = input("Your option: ")

            if option == "1":
                new_map.randomMap()
                self.__controller.setMap(new_map)
                print("Map successfully generated!\n")

            elif option == "2":
                map_filename = input("Enter the map filename: ")
                new_map.loadMap(map_filename)
                self.__controller.setMap(new_map)
                print("Map successfully loaded!\n")

            elif option == "3":
                map_filename = input("Enter the map filename: ")
                new_map.saveMap(map_filename)
                print("Map successfully saved!\n")
            elif option == "4":
                # gui = GUI(self.__controller)
                # #TODO make this display the map
                # gui.image(new_map)
                print(new_map)
            elif option == "0":
                break
            else:
                print("Invalid command!\n")

    def runEAOptions(self):
        while True:
            self.printEAMenu()
            option = input("Your choice: ")

            if option == "1":
                self.population_size = input("Population size: ")
                self.individual_size = input("Number of individuals: ")
                self.number_of_generations = input("Number of generations: ")
                self.number_of_iterations = input("Number of iterations: ")

            elif option == "2":
                self.best_individual, averages = self.__controller.solver(self.population_size, self.individual_size, self.number_of_generations, self.number_of_iterations)

                self.plotGraph(averages)
                self.logToFile(averages)

            elif option == "3":
                gui = GUI(self.__controller)
                gui.movingDrone(self.__controller.getMap(), self.best_individual)

            elif option == "0":
                break
            else:
                print("Invalid command.\n")

    def start(self):
        while True:
            self.printMenu()
            option = input("Your choice: ")
            if option == "1":
                self.runMapOptions()
            elif option == "2":
                self.runEAOptions()
            elif option == "0":
                break
            else:
                print("Invalid command!\n")
