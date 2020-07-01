from Settings import settings
class players:
    def __init__(self):
        self.settings = settings()
        self.player_width = 10
        self.player_height = 80
        self.player_speed = 8

        self.left_player_score = 0
        self.right_player_score = 0

    def move_players(self, left_y, right_y, l_change, r_change):
        left_y += l_change
        right_y += r_change

        if left_y + self.player_height > self.settings.HEIGHT:
            left_y = self.settings.HEIGHT - self.player_height
        if left_y < 0:
            left_y = 0

        if right_y + self.player_height > self.settings.HEIGHT:
            right_y = self.settings.HEIGHT - self.player_height
        if right_y < 0:
            right_y = 0
        return left_y, right_y
