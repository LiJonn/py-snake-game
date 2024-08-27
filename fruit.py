import pygame
import random
from settings import *

class Fruit:
    def __init__(self, play_area_x, play_area_y, play_area_width, play_area_height):
        self.play_area_x = play_area_x
        self.play_area_y = play_area_y
        self.play_area_width = play_area_width
        self.play_area_height = play_area_height
        self.respawn()  # Initialize the position when the fruit is created

    def respawn(self):
        x = random.randrange(self.play_area_x, self.play_area_x + self.play_area_width, 10)
        y = random.randrange(self.play_area_y, self.play_area_y + self.play_area_height, 10)
        self.position = [x, y]  # Update self.position directly

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, pygame.Rect(self.position[0], self.position[1], 10, 10))
