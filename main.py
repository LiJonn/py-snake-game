from game import Game
import pygame
import sys
from settings import *

def main_menu():
    pygame.init()

    # Load and set the game window icon
    icon = pygame.image.load('./assets/image/snake_game_icon.png')
    pygame.display.set_icon(icon)

    # Set the game window title
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

    while True:
        game_window.fill(BLACK)

        # Display menu options
        font = pygame.font.SysFont('times new roman', 50)
        title_surface = font.render('Snake Game', True, GREEN)
        game_window.blit(title_surface, (WINDOW_X//2 - title_surface.get_width()//2, WINDOW_Y//4))

        button_font = pygame.font.SysFont('times new roman', 35)
        start_button = pygame.Rect(WINDOW_X//2 - 75, WINDOW_Y//2 - 50, 150, 50)
        quit_button = pygame.Rect(WINDOW_X//2 - 75, WINDOW_Y//2 + 50, 150, 50)

        pygame.draw.rect(game_window, GREEN, start_button)
        pygame.draw.rect(game_window, RED, quit_button)

        start_surface = button_font.render('Start', True, BLACK)
        quit_surface = button_font.render('Quit', True, BLACK)

        game_window.blit(start_surface, (start_button.x + start_button.width//2 - start_surface.get_width()//2, start_button.y + start_button.height//2 - start_surface.get_height()//2))
        game_window.blit(quit_surface, (quit_button.x + quit_button.width//2 - quit_surface.get_width()//2, quit_button.y + quit_button.height//2 - quit_surface.get_height()//2))

        pygame.display.flip()

        # Event handling for menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game = Game()
                    game.run()
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()
