import sys
import pygame
import game_function as gf
from settings import settings
from Ship import ship

def run_game():
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    shipdraw = ship(screen)

    while True:
        gf.check_events(shipdraw)
        gf.update_screen(ai_settings, screen, shipdraw)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        shipdraw.blitme()

    pygame.display.flip()


run_game()
