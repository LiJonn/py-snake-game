import pygame
import random
from settings import *

class Fruit:
    def __init__(self, play_area_x, play_area_y, play_area_width, play_area_height):
        self.play_area_x = play_area_x
        self.play_area_y = play_area_y
        self.play_area_width = play_area_width
        self.play_area_height = play_area_height

        # Load and scale the fruit image to the new size
        self.image = pygame.image.load('./assets/image/apple_red.png')
        self.image = pygame.transform.scale(self.image, (20, 20))  # Scale to 20x20 pixels

        self.respawn()  # Initialize the position when the fruit is created

    def respawn(self):
        x = random.randrange(self.play_area_x, self.play_area_x + self.play_area_width, 20)
        y = random.randrange(self.play_area_y, self.play_area_y + self.play_area_height, 20)
        self.position = [x, y]  # Update self.position directly

    def draw(self, surface):
        surface.blit(self.image, (self.position[0], self.position[1]))  # Draw the fruit image
