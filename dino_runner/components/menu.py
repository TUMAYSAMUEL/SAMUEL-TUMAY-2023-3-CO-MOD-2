import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT 

class menu:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2

    def __init__(self, screen, message):
        screen.fill((255, 255, 255))
        self.fond = pygame.fond.Fond(FONT_STYLE, 30)
        self.text = self.fond.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.x = self.half_screen_width
        self.text_rect.y = self.half_screen_height

