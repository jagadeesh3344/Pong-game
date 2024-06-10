import pygame, sys, random

class PongGame:
    def __init__(self):
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong Game")

        self.clock = pygame.time.Clock()

        self.ball = pygame.Rect(0, 0, 30, 30)
        self.ball.center = (self.screen_width / 2, self.screen_height / 2)

        self.computer = pygame.Rect(0, 0, 20, 100)
        self.computer.centery = self.screen_height / 2

        self.player = pygame.Rect(0, 0, 20, 100)
        self.player.midright = (self.screen_width, self.screen_height / 2)

        self.general_speed = 6

        self.ball_speed_x = self.general_speed
        self.ball_speed_y = self.general_speed
        self.player_speed = 0
        self.computer_speed = self.general_speed

        self.player_score = 0
        self.computer_score = 0

    def reset_ball(self):
        self.ball.center = (self.screen_width / 2, self.screen_height / 2)
        self.ball_speed_x = self.general_speed * random.choice([-1, 1])
        self.ball_speed_y = self.general_speed * random.choice([-1, 1])

    def point_winner(self, scorer, final_score):
        self.player_score += scorer == "player"
        self.computer_score += scorer == "computer"
        if max(self.player_score, self.computer_score) == final_score:
            return "player" if self.player_score == final_score else "computer"
        self.reset_ball()
        return ''

    def animate_ball(self, final_score):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.bottom >= self.screen_height or self.ball.top <= 0:
            self.ball_speed_y *= -1
            
        winner = ''

        if self.ball.right >= self.screen_width:
            winner = self.point_winner("computer", final_score)
        elif self.ball.left <= 0:
            winner = self.point_winner("player", final_score)

        if self.ball.colliderect(self.player) or self.ball.colliderect(self.computer):
            self.ball_speed_x *= -1

        return winner

    def animate_player(self):
        self.player.y += self.player_speed

        if self.player.top <= 0:
            self.player.top = 0

        if self.player.bottom >= self.screen_height:
            self.player.bottom = self.screen_height

    def animate_computer(self):
        self.computer.y += self.computer_speed

        if self.ball.centery <= self.computer.centery:
            self.computer_speed = -self.general_speed
        elif self.ball.centery >= self.computer.centery:
            self.computer_speed = self.general_speed

        if self.computer.top <= 0:
            self.computer.top = 0
        elif self.computer.bottom >= self.screen_height:
            self.computer.bottom = self.screen_height

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player_speed = -self.general_speed
                elif event.key == pygame.K_DOWN:
                    self.player_speed = self.general_speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player_speed = 0

    def draw_objects(self):
        self.screen.fill('black')

        font = pygame.font.Font(None, 50)
        text = f"Computer      Player"
        rendered_text = font.render(text, True, (255, 255, 255))
        self.screen.blit(rendered_text, (250, 30))
        text = f"  {self.computer_score}                  {self.player_score}"
        rendered_text = font.render(text, True, (255, 255, 255))
        self.screen.blit(rendered_text, (310, 75))

        pygame.draw.ellipse(self.screen, 'white', self.ball)
        pygame.draw.rect(self.screen, 'white', self.computer)
        pygame.draw.rect(self.screen, 'white', self.player)

    def update_display(self):
        pygame.display.update()
        self.clock.tick(60)

    def run(self, final_score):
        while True:
            self.handle_events()
            winner = self.animate_ball(final_score)
            self.animate_player()
            self.animate_computer()
            self.draw_objects()
            self.update_display()

            if winner != '':
                print(f"{winner} wins!")
                pygame.time.wait(1000)
                pygame.quit()
                return winner

if __name__ == "__main__":
    game = PongGame()
    game.run(10)  # You can adjust the final score here
