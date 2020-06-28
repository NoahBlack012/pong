import pygame
from Settings import settings
from Players import players
from Ball import ball
class draw:
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.players = players()
        self.ball = ball()
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

    def draw_ball(self, screen, x, y):
        pygame.draw.circle(screen, self.settings.ball_col, (x, y), self.ball.radius)

    def middle_line(self, screen):
        lines = range(0, self.settings.HEIGHT, int(self.player_height*1.5))
        for line in lines:
            pygame.draw.rect(screen, self.settings.line_col, (int(self.settings.WIDTH/2 - self.player_width/2), int(line), self.player_width, self.player_height))

    def left_score(self, screen, text, col, font):
        l_score = font.render(str(text), False, col)
        screen.blit(l_score, (int(self.settings.WIDTH/2 - self.settings.WIDTH/58 * 2), int(self.settings.HEIGHT/60 * 2)))

    def right_score(self, screen, text, col, font):
        r_score = font.render(str(text), False, col)
        screen.blit(r_score, (int(self.settings.WIDTH/2 + self.settings.WIDTH/58), int(self.settings.HEIGHT/60 * 2)))
