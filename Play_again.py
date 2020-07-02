import pygame
from Settings import settings

class play_again:
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.gameover = True

    def draw_play_again(self, screen, col, font):
        rect = pygame.Rect(int(self.settings.WIDTH/3), int(self.settings.HEIGHT/2 - self.settings.HEIGHT/12),
            int(self.settings.WIDTH/3), int(self.settings.HEIGHT/6))
        text_col = col
        button_col = self.settings.button_col
        filled = 0
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > rect[0] and mouse_x < rect[0] + rect[2] and mouse_y > rect[1] and mouse_y < rect[1] + rect[3]:
            text_col = self.settings.button_col
            button_col = self.settings.bg_col
            buttons = pygame.mouse.get_pressed()
            if buttons[0] == True:
                self.gameover = False
        text_rect = pygame.Rect(rect[0], rect[1] + rect[3]/4, rect[2], rect[3])
        pygame.draw.rect(screen, button_col, (rect))
        text = font.render(str("Play Again"), False, text_col)
        screen.blit(text, (text_rect))
        return self.gameover
