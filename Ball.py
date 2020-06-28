from Settings import settings
import math
import random
class ball:
    def __init__(self):
        self.settings = settings()
        self.radius = 10
        self.x = int(self.settings.WIDTH/2)
        self.y = int(self.settings.HEIGHT/2)
        self.speed = 6
        self.direction = 0

    def reset(self):
        positive_dirs = []
        negative_dirs = []
        for num in range(30, 45):
            positive_dirs.append(num)
        for num in range(-30, -45):
            negative_dirs.append(num)
        directions = positive_dirs + negative_dirs
        self.direction = random.choice(directions)
        if random.randrange(2) == 0:
            self.direction += 180
        self.x = int(self.settings.WIDTH/2)
        self.y = int(self.settings.HEIGHT/2)
        self.speed = 6

    def wall_redirect(self):
        self.direction = (180-self.direction)%360
        self.speed *= 1.05

    def paddle_redirect(self):
        self.direction = -self.direction
        self.speed *= 1.05

    def move_ball(self):
        """Moves the ball to the current position"""
        radians = math.radians(self.direction)
        self.x += self.speed * math.sin(radians)
        self.y -= self.speed * math.cos(radians)
