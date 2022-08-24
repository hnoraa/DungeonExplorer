import pygame
import sys

from constants import *


class Main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SC_W, SC_H))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.running = False
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    x = Main()
    x.run()
