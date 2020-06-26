import pygame
from Settings import settings
class draw:
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.player_width = 10
        self.player_height = 80
        self.right_player_keys = [pygame.K_UP, pygame.K_DOWN]
        self.left_player_keys = [pygame.K_w, pygame.K_s]

    def move_players(self, left_y, right_y):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == spygame.K_w:
                    left_y -= 1
                    print ("l up")
                if event.key == self.left_player_keys[1]:
                    left_y += 1
                    print ("l down")
                if event.key == self.right_player_keys[0]:
                    right_y -= 1
                    print ("r up")
                if event.key == self.right_player_keys[1]:
                    right_y += 1
                    print ("r down")
        return left_y, right_y

    def left_player(self, screen, y):
        x = int(self.settings.WIDTH/60)
        pygame.draw.rect(screen, self.settings.player_col, (x, y, self.player_width, self.player_height))

    def right_player(self, screen, y):
        x = int(self.settings.WIDTH/60 * 58 + 10)
        pygame.draw.rect(screen, self.settings.player_col, (x, y, self.player_width, self.player_height))
