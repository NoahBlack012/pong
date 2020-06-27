from Settings import settings
class ball:
    def __init__(self):
        self.settings = settings()
        self.radius = 10
        self.x = int(self.settings.WIDTH/2)
        self.y = int(self.settings.HEIGHT/2)
