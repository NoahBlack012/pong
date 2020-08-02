from Settings import settings
from Players import players
import math
import random
import pygame
class ball:
    def __init__(self):
        self.settings = settings()
        self.players = players()
        pygame.init()
        self.radius = 10
        self.x = int(self.settings.WIDTH/2)
        self.y = int(self.settings.HEIGHT/2)
        self.speed = 8
        self.direction = 0
        self.bounce_sound = pygame.mixer.Sound(r'C:\Users\Eastb\Documents\Python\pong\blip.wav')

    def reset(self):
        positive_dirs = []
        negative_dirs = []
        for num in range(30, 45):
            positive_dirs.append(num)
        for num in range(-30, -45):
            negative_dirs.append(num)
        directions = positive_dirs + negative_dirs
        self.direction = random.choice(directions)
        if random.randrange(2) % 2== 0:
            self.direction += 180
        self.x = int(self.settings.WIDTH/2)
        self.y = int(self.settings.HEIGHT/2)
        self.speed = 6

    def wall_redirect(self):
        self.direction = (180-self.direction)%360
        self.speed *= 1.1
        self.bounce_sound.play()

    def paddle_redirect(self):
        self.bounce_sound.play()
        self.direction = -self.direction
        self.speed *= 1.05

    def move_ball(self):
        """Moves the ball to the current position"""
        radians = math.radians(self.direction)
        self.x += self.speed * math.sin(radians)
        self.y -= self.speed * math.cos(radians)
