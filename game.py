import pygame
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
        self.fruit = Fruit(PLAY_AREA_X, PLAY_AREA_Y, PLAY_AREA_WIDTH, PLAY_AREA_HEIGHT)
        self.running = True
        self.high_score = 0
        self.speed = 10  # Initial speed

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            # Check if the game should end
            if not self.running:
                self.handle_game_over()

            # Adjust speed based on the score
            self.adjust_speed()

            # Control the game's speed
            self.fps.tick(self.speed)

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
        if self.snake.has_collided_with_wall(PLAY_AREA_X, PLAY_AREA_Y, PLAY_AREA_WIDTH, PLAY_AREA_HEIGHT) or self.snake.has_collided_with_self():
            self.running = False  # End the game loop
        if self.snake.has_eaten_fruit(self.fruit.position):
            self.snake.grow()
            self.snake.increment_score()
            self.fruit.respawn()  # Correctly respawn the fruit

    def render(self):
        self.game_window.fill(BLACK)

        # Draw the play area with a different background color
        pygame.draw.rect(self.game_window, DARK_GRAY, (PLAY_AREA_X, PLAY_AREA_Y, PLAY_AREA_WIDTH, PLAY_AREA_HEIGHT))

        self.snake.draw(self.game_window)
        self.fruit.draw(self.game_window)
        show_score(self.game_window, 'Score', WHITE, 'times new roman', 20, self.snake.score)
        show_score(self.game_window, 'Highest Score', WHITE, 'times new roman', 20, self.high_score, x_offset=150)

        pygame.display.update()


    def adjust_speed(self):
        # Adjust Speed of Snake Based on Score
        speed_thresholds = [
            (100, 12),
            (200, 15),
            (300, 28),
            (400, 21),
            (500, 24),
            (600, 27),
            (700, 30),
            (800, 33),
            (900, 36),
        ]

        # Default to the highest speed if no other thresholds match
        self.speed = 40

        # Find the appropriate speed based on the score
        for threshold, speed in speed_thresholds:
            if self.snake.score < threshold:
                self.speed = speed
                break


    def handle_game_over(self):
        # Update high score if the current score is greater
        if self.snake.score > self.high_score:
            self.high_score = self.snake.score

        game_over(self.snake.score, self.high_score)
        self.reset_game()
        self.run()

    def reset_game(self):
        self.snake = Snake()
        self.fruit = Fruit(PLAY_AREA_X, PLAY_AREA_Y, PLAY_AREA_WIDTH, PLAY_AREA_HEIGHT)
        self.running = True
