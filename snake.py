import pygame
from settings import *

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

        # Load the snake head and body images
        self.head_image = pygame.image.load('./assets/image/snake_green_head.png')
        self.head_image = pygame.transform.scale(self.head_image, (10, 10))
        self.body_image = pygame.image.load('./assets/image/snake_green_body.png')
        self.body_image = pygame.transform.scale(self.body_image, (10, 10))

    def change_direction(self, new_direction):
        if new_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move(self):
        if self.direction == 'UP':
            self.position[1] -= 10
        elif self.direction == 'DOWN':
            self.position[1] += 10
        elif self.direction == 'LEFT':
            self.position[0] -= 10
        elif self.direction == 'RIGHT':
            self.position[0] += 10

        self.body.insert(0, list(self.position))
        self.body.pop()

    def grow(self):
        self.body.insert(0, list(self.position))

    def has_eaten_fruit(self, fruit_position):
        return self.position == fruit_position

    def has_collided_with_wall(self, play_area_x, play_area_y, play_area_width, play_area_height):
        if self.position[0] < play_area_x or self.position[0] >= play_area_x + play_area_width:
            return True
        if self.position[1] < play_area_y or self.position[1] >= play_area_y + play_area_height:
            return True
        return False

    def has_collided_with_self(self):
        return self.position in self.body[1:]

    def increment_score(self):
        self.score += 10

    def draw(self, surface):
        # Draw the head
        surface.blit(self.head_image, (self.body[0][0], self.body[0][1]))
        # Draw the body
        for pos in self.body[1:]:
            surface.blit(self.body_image, (pos[0], pos[1]))
