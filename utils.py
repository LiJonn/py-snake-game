import pygame
import sys
from settings import *

def show_score(surface, choice, color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    surface.blit(score_surface, score_rect)

def game_over(score):
    game_window = pygame.display.get_surface()
    my_font = pygame.font.SysFont('times new roman', 50)

    # Display Game Over Message
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_X/2, WINDOW_Y/4)
    game_window.blit(game_over_surface, game_over_rect)

    # Display Restart and Quit Buttons
    button_font = pygame.font.SysFont('times new roman', 35)
    restart_button = pygame.Rect(WINDOW_X//2 - 75, WINDOW_Y//2 - 50, 150, 50)
    quit_button = pygame.Rect(WINDOW_X//2 - 75, WINDOW_Y//2 + 50, 150, 50)

    pygame.draw.rect(game_window, GREEN, restart_button)
    pygame.draw.rect(game_window, RED, quit_button)

    restart_surface = button_font.render('Restart', True, BLACK)
    quit_surface = button_font.render('Quit', True, BLACK)

    game_window.blit(restart_surface, (restart_button.x + restart_button.width//2 - restart_surface.get_width()//2, restart_button.y + restart_button.height//2 - restart_surface.get_height()//2))
    game_window.blit(quit_surface, (quit_button.x + quit_button.width//2 - quit_surface.get_width()//2, quit_button.y + quit_button.height//2 - quit_surface.get_height()//2))

    pygame.display.flip()

    # Event handling for game over menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return  # Exit the function to restart the game
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
