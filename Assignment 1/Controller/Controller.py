from Domain.Map import *
from Domain.Environment import *
from Domain.Drone import *
from Domain.Constants import *

class Controller:
    def __init__(self):
        # we create the environment
        self.__environment = Environment()

        # we create the map
        self.__map = DMap()

        # we position the drone somewhere in the area
        [x, y] = self.__environment.getRandomEmptySquare()

        # place the drone on an empty square
        self.__drone = Drone(x, y)

        # containers that will be used for moving the drone
        self.stack = deque()
        self.stack.append((x, y))

        self.visited = []

    def getDrone(self):
        return self.__drone

    def getEnvironment(self):
        return self.__environment

    def getDetectedMap(self):
        return self.__map

    #def moveDFS(self):
    #    return self.__drone.moveDFS(self.__map)

    def moveDFS(self):
        current_x = self.__drone.getX()
        current_y = self.__drone.getY()

        self.visited.append((current_x, current_y))

        # try to visit the adjacent nodes in the order UP, LEFT, DOWN, RIGHT
        for position in directions:
            next_x = current_x + position[0]
            next_y = current_y + position[1]

            # check that the new position is valid, it is not a wall and the square has not been visited
            if is_valid_position(next_x, next_y):
                if self.__map.is_empty_position(next_x, next_y) and (next_x, next_y) not in self.visited:
                    # add the current position to the stack as well, to trace back when the drone gets stuck
                    self.stack.append((current_x, current_y))
                    # add the next position
                    self.stack.append((next_x, next_y))
                    break

        # when the stack is empty, all nodes have been visited
        if not self.stack:
            return False

        # update the current position
        else:
            next_square = self.stack.pop()
            self.__drone.setX(next_square[0])
            self.__drone.setY(next_square[1])
            return True

    def mark_detected_walls(self):
        self.__map.markDetectedWalls(self.__environment, self.__drone)

    def get_map_image(self):
        return self.__map.image(self.__drone)

    def get_environment_image(self):
        return self.__environment.image()
