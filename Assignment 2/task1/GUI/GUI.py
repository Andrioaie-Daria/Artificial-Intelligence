import time
import pygame
from Controller.Controller import *


def displayWithPath(image, path):
    mark = pygame.Surface((20, 20))
    mark.fill(GREEN)
    for move in path:
        image.blit(mark, (move[1] * 20, move[0] * 20))

    return image


def init_pygame():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Path in simple environment")

class GUI():
    def __init__(self):
        self.__controller = Controller()
        init_pygame()
        self.__screen = self.initScreen()
        self.placeText()

    def placeText(self):
        pygame.font.init()
        font = pygame.font.SysFont('arial', 25)
        a_star_text = font.render('A* Search', True, BLACK)
        a_star_rectangle = a_star_text.get_rect()
        a_star_rectangle.center = (200, 20)
        self.__screen.blit(a_star_text, a_star_rectangle)

        greedy_text = font.render('Greedy Search', True, BLACK)
        greedy_rectangle = greedy_text.get_rect()
        greedy_rectangle.center = (650, 20)
        self.__screen.blit(greedy_text, greedy_rectangle)

    def initScreen(self):
        # create a surface on screen that has the size of 400 x 480
        screen = pygame.display.set_mode((850, 450))
        screen.fill(WHITE)
        screen.blit(self.__controller.getMapImage(), (0, 50))
        screen.blit(self.__controller.getMapImage(), (450, 50))

        return screen

    def updateDronePositionOnMap(self):
        self.__screen.blit(self.__controller.placeDroneOnMap(), (0, 50))
        self.__screen.blit(self.__controller.placeDroneOnMap(), (450, 50))
        pygame.display.flip()

    def displayAStarPath(self, path):
        self.__screen.blit(displayWithPath(self.__controller.getMapImage(), path), (0, 50))

    def displayGreedyPath(self, path):
        self.__screen.blit(displayWithPath(self.__controller.getMapImage(), path), (450, 50))

    def run(self):
        self.updateDronePositionOnMap()
        time.sleep(2)

        [goal_x, goal_y] = self.__controller.getRandomEmptySquare()

        time0 = time.time()
        a_star_path = self.__controller.aSearch(goal_x, goal_y)
        a_star_time = time.time() - time0
        print(a_star_time)
        self.displayAStarPath(a_star_path)

        time0 = time.time()
        greedy_path = self.__controller.greedySearch(goal_x, goal_y)
        greedy_time = time.time() - time0
        print(greedy_time)
        self.displayGreedyPath(greedy_path)



        pygame.display.flip()
        time.sleep(20)
        pygame.quit()