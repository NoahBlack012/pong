import pygame
from Settings import settings
import sys

class menu:
    def __init__(self):
        self.settings = settings()
        pygame.init()
        pygame.font.init()
        self.exit = False

    def draw_title(self, screen, col, font):
        text = font.render(str("Welcome to Pong"), False, col)
        screen.blit(text, (int(self.settings.WIDTH/4), int(self.settings.HEIGHT/3)))

    def draw_play(self, screen, col, font):
        rect = pygame.Rect(int(self.settings.WIDTH/3), int(self.settings.HEIGHT/2),
            int(self.settings.WIDTH/3), int(self.settings.HEIGHT/6))
        text_col = col
        button_col = self.settings.button_col
        filled = 0
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > rect[0] and mouse_x < rect[0] + rect[2] and mouse_y > rect[1] and mouse_y < rect[1] + rect[3]:
            text_col = self.settings.button_col
            filled = 5
            buttons = pygame.mouse.get_pressed()
            if buttons[0] == True:
                self.exit = True
        text_rect = pygame.Rect(rect[0] + rect[2]/3, rect[1] + rect[3]/4, rect[2], rect[3])
        pygame.draw.rect(screen, button_col, (rect), filled)
        text = font.render(str("Play"), False, text_col)
        screen.blit(text, (text_rect))

    # def menu_test(self):
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 sys.exit()
    #         self.screen.fill(self.settings.bg_col)
    #         self.menu.draw_play(self.screen, self.settings.button_text_col, self.title_font)
    #         self.menu.draw_title(self.screen, self.settings.font_col, self.title_font)
    #         pygame.display.flip()
