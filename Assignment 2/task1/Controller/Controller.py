from random import randint
from Domain.Drone import Drone
from Domain.Map import Map
from Domain.Constants import *

class Controller():
    def __init__(self):
        # we create the map
        self.__map = Map()
        # m.randomMap()
        # m.saveMap("test2.map")
        self.__map.loadMap("test1.map")

        # we position the drone somewhere in the area
        [x, y] = self.__map.getRandomEmptySquare()

        # create drona
        self.__drone = Drone(x, y)

    def dummySearch(self):
        # example of some path in test1.map from [5,7] to [7,11]
        return [[5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [6, 11], [7, 11]]

    def isValidNode(self, x, y):
        return -1 < x < 20 and -1 < y < 20 and self.__map.isEmptyPosition(x, y)

    def buildPath(self, previous, goal_x, goal_y):
        path = [(goal_x, goal_y)]
        next_node = previous[(goal_x, goal_y)]
        while next_node != (None, None):
            path.append(next_node)
            next_node = previous[next_node]

        path.reverse()
        return path

    def aSearch(self, goal_x, goal_y):
        [start_x, start_y] = self.__drone.getCoordinates()
        to_visit_queue = [(start_x, start_y)]

        previous = dict()
        previous[(start_x, start_y)] = (None, None)

        distance = dict()
        distance[(start_x, start_y)] = 0

        visited = []
        found = False

        while to_visit_queue and not found:
            current_node = to_visit_queue.pop(0)
            visited.append(current_node)
            if current_node == (goal_x, goal_y):
                found = True
            else:
                aux = []
                for direction in directions:
                    next_x = current_node[0] + direction[0]
                    next_y = current_node[1] + direction[1]

                    if self.isValidNode(next_x, next_y) and (next_x, next_y) not in visited:
                        if (next_x, next_y) not in to_visit_queue:
                            aux.append((next_x, next_y))
                            previous[(next_x, next_y)] = current_node
                            distance[(next_x, next_y)] = distance[current_node] + 1
                        else:
                            if distance[(next_x, next_y)] > distance[current_node] + 1:
                                to_visit_queue.remove((next_x, next_y))
                                aux.append((next_x, next_y))
                                previous[(next_x, next_y)] = current_node
                                distance[(next_x, next_y)] = distance[current_node] + 1

                to_visit_queue.extend(aux)
                to_visit_queue.sort(key=lambda current: self.manhattanDistance(current[0], current[1], goal_x, goal_y) + distance[current])

        if found:
            return self.buildPath(previous, goal_x, goal_y)
        else:
            return []

    def greedySearch(self, goal_x, goal_y):
        [start_x, start_y] = self.__drone.getCoordinates()
        to_visit_queue = [(start_x, start_y)]

        previous = dict()
        previous[(start_x, start_y)] = (None, None)

        visited = []
        found = False

        while to_visit_queue and not found:
            current_node = to_visit_queue.pop(0)
            visited.append(current_node)
            if current_node == (goal_x, goal_y):
                found = True
            else:
                aux = []
                for direction in directions:
                    next_x = current_node[0] + direction[0]
                    next_y = current_node[1] + direction[1]

                    if self.isValidNode(next_x, next_y) and (next_x, next_y) not in visited:
                        aux.append((next_x, next_y))
                        previous[(next_x, next_y)] = current_node

                to_visit_queue.extend(aux)
                to_visit_queue.sort(key=lambda current: self.manhattanDistance(current[0], current[1], goal_x, goal_y))

        if found:
            return self.buildPath(previous, goal_x, goal_y)
        else:
            return []

    def manhattanDistance(self, current_x, current_y, goal_x, goal_y):
        return abs(current_x - goal_x) + abs(current_y-goal_y)

    def getMapImage(self):
        return self.__map.image()

    def placeDroneOnMap(self):
        return self.__drone.mapWithDrone(self.__map.image())

    def getRandomEmptySquare(self):
        return self.__map.getRandomEmptySquare()
