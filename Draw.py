import pygame
from Settings import settings
from Players import players
class draw:
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.players = players()
        self.player_width = self.players.player_width
        self.player_height = self.players.player_height
        self.right_player_keys = [pygame.K_UP, pygame.K_DOWN]
        self.left_player_keys = [pygame.K_w, pygame.K_s]


    def left_player(self, screen, y):
        x = int(self.settings.WIDTH/60)
        pygame.draw.rect(screen, self.settings.player_col, (x, y, self.player_width, self.player_height))

    def right_player(self, screen, y):
        x = int(self.settings.WIDTH/60 * 58 + 10)
        pygame.draw.rect(screen, self.settings.player_col, (x, y, self.player_width, self.player_height))
