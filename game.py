import pygame
import time
from settings import *
from snake import Snake
from fruit import Fruit
from utils import show_score, game_over

class Game:
    def __init__(self):
        pygame.init()
        self.game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
        pygame.display.set_caption('Snake Game')
        self.fps = pygame.time.Clock()
        self.snake = Snake()
        self.fruit = Fruit()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            # Check if the game should end
            if not self.running:
                self.handle_game_over()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')

    def update(self):
        self.snake.move()
        if self.snake.has_collided_with_wall() or self.snake.has_collided_with_self():
            self.running = False  # End the game loop
        if self.snake.has_eaten_fruit(self.fruit.position):
            self.snake.grow()
            self.snake.increment_score()
            self.fruit.respawn()

    def render(self):
        self.game_window.fill(BLACK)
        self.snake.draw(self.game_window)
        self.fruit.draw(self.game_window)
        show_score(self.game_window, 1, WHITE, 'times new roman', 20, self.snake.score)
        pygame.display.update()
        self.fps.tick(SNAKE_SPEED)

    def handle_game_over(self):
        game_over(self.snake.score)
        self.reset_game()
        self.run()

    def reset_game(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.running = True
