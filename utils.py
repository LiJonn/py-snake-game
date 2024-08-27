import pygame
import sys
from settings import *

def show_score(surface, label, color, font, size, score, x_offset=0):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'{label} : {score}', True, color)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (x_offset + 10, 10)
    surface.blit(score_surface, score_rect)


def game_over(score, high_score):
    game_window = pygame.display.get_surface()
    my_font = pygame.font.SysFont('times new roman', 40)

    # Display Game Over Message
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, WHITE)

    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_X/2, WINDOW_Y/4)
    game_window.blit(game_over_surface, game_over_rect)

    # # Display High Score
    # high_score_surface = my_font.render('High Score : ' + str(high_score), True, WHITE)
    # high_score_rect = high_score_surface.get_rect()
    # high_score_rect.midtop = (WINDOW_X/2, WINDOW_Y/4 + 50)
    # game_window.blit(high_score_surface, high_score_rect)

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
