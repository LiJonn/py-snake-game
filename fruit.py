import pygame
import random
from settings import *

class Fruit:
    def __init__(self):
        self.position = [random.randrange(1, (WINDOW_X//10)) * 10, random.randrange(1, (WINDOW_Y//10)) * 10]

    def respawn(self):
        self.position = [random.randrange(1, (WINDOW_X//10)) * 10, random.randrange(1, (WINDOW_Y//10)) * 10]

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, pygame.Rect(self.position[0], self.position[1], 10, 10))
