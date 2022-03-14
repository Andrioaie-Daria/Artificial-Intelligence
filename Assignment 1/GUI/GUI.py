import pygame
from pygame.locals import *
import time
from Controller import *
from Controller.Controller import Controller
from Domain.Constants import *


class GUI():
    def __init__(self):
        self.__controller = Controller()
        self.__screen = self.__init_screen()
        self.__init_pygame()

    def __init_screen(self):
        # create a surface on screen that has the size of 800 x 480
        screen = pygame.display.set_mode((800, 400))
        screen.fill(WHITE)
        screen.blit(self.__controller.get_environment_image(), (0, 0))
        return screen

    def __init_pygame(self):
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("drone exploration")

    def update_map(self):
        self.__controller.mark_detected_walls()
        self.__screen.blit(self.__controller.get_map_image(), (400, 0))
        pygame.display.flip()

    def moveDFS(self):
        return self.__controller.moveDFS()

    def run(self):

        # define a variable to control the main loop
        running = True

        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # stop the execution
                    pygame.quit()

            running = self.moveDFS()
            pygame.time.wait(250)

            if running:
                self.update_map()

        pygame.quit()
