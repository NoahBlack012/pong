import pygame
import sys
from Settings import settings
from Draw import draw
from Players import players
from Ball import ball
from Menu import menu
from Play_again import play_again

class Pong:
    """A class to manage overall aspects within the game and run the game"""
    def __init__(self):
        """Init objects and some variables for the game"""
        pygame.init()
        pygame.font.init()
        self.settings = settings()
        self.draw = draw()
        self.players = players()
        self.ball = ball()
        self.menu = menu()
        self.play_again = play_again()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("Pong")
        self.left_player_y = int(self.settings.HEIGHT/2)
        self.right_player_y = int(self.settings.HEIGHT/2)
        self.left_player_x = int(self.settings.WIDTH/60)
        self.right_player_x = int(self.settings.WIDTH/60 * 58 + 10)

        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.l_change = 0
        self.r_change = 0
        self.game_started = False
        self.target_score = 5
        self.gameover = False
        self.game_exit = False

        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.title_font = pygame.font.Font('freesansbold.ttf', 60)
        self.explosion_sound = pygame.mixer.Sound(r'C:\Users\Eastb\Documents\Python\pong\explosion.wav')

    def run_game(self):
        """Run the game"""
        while not self.menu.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_col)
            self.menu.draw_play(self.screen, self.settings.button_text_col, self.title_font)
            self.menu.draw_title(self.screen, self.settings.font_col, self.title_font)
            pygame.display.flip()
        self.ball.reset()
        while not self.game_exit:
            self.players.left_player_score = 0
            self.players.right_player_score = 0
            self.play_again.gameover = True
            while not self.gameover:
                self.clock.tick(self.FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == self.draw.left_player_keys[0]:
                            self.l_change = -self.players.player_speed
                        if event.key == self.draw.left_player_keys[1]:
                            self.l_change = self.players.player_speed
                        if event.key == self.draw.right_player_keys[0]:
                            self.r_change = -self.players.player_speed
                        if event.key == self.draw.right_player_keys[1]:
                            self.r_change = self.players.player_speed

                self.left_player_y, self.right_player_y = self.players.move_players(self.left_player_y, self.right_player_y, self.l_change, self.r_change)

                self.screen.fill(self.settings.bg_col)

                ###Draw items here###
                self.draw.right_score(self.screen, self.players.right_player_score, self.settings.font_col, self.font)
                self.draw.left_score(self.screen, self.players.left_player_score, self.settings.font_col, self.font)
                self.draw.left_player(self.screen, self.left_player_y)
                self.draw.right_player(self.screen, self.right_player_y)
                self.draw.draw_ball(self.screen, int(self.ball.x), int(self.ball.y))
                self.draw.middle_line(self.screen)
                #####################

                if self.ball.y - self.ball.radius < 0 or self.ball.y + self.ball.radius > self.settings.HEIGHT:
                    self.ball.wall_redirect()

                if self.ball.x - self.ball.radius <= self.left_player_x + self.players.player_width and self.ball.y > self.left_player_y and self.ball.y < self.left_player_y + self.players.player_height:
                    self.ball.paddle_redirect()

                if self.ball.x + self.ball.radius >= self.right_player_x and self.ball.y > self.right_player_y and self.ball.y < self.right_player_y + self.players.player_height:
                    self.ball.paddle_redirect()

                self.ball.move_ball()

                if self.ball.x > self.settings.WIDTH:
                    self.ball.reset()
                    self.explosion_sound.play()
                    self.players.left_player_score += 1

                if self.ball.x < 0:
                    self.ball.reset()
                    self.explosion_sound.play()
                    self.players.right_player_score += 1

                if self.players.left_player_score >= self.target_score:
                    self.gameover = True

                if self.players.right_player_score >= self.target_score:
                    self.gameover = True

                if self.players.left_player_score + 1 == self.target_score and self.players.right_player_score + 1 == self.target_score:
                    self.target_score += 1
                pygame.display.flip()

            self.screen.fill(self.settings.bg_col)
            self.draw.right_score(self.screen, self.players.right_player_score, self.settings.font_col, self.font)
            self.draw.left_score(self.screen, self.players.left_player_score, self.settings.font_col, self.font)
            self.draw.left_player(self.screen, self.left_player_y)
            self.draw.right_player(self.screen, self.right_player_y)
            self.draw.draw_ball(self.screen, int(self.ball.x), int(self.ball.y))
            self.draw.middle_line(self.screen)
            self.gameover = self.play_again.draw_play_again(self.screen, self.settings.button_text_col, self.title_font)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()



if __name__ == '__main__':
    p = Pong()
    p.run_game()
