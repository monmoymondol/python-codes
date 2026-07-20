import pygame
from player import Player
from ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Football Game")
        self.clock = pygame.time.Clock()

        # players
        self.player1 = Player(100, 300, (255, 0, 0))
        self.player2 = Player(700, 300, (0, 0, 255))
        self.ball = Ball(400, 300)

        self.all_sprites = pygame.sprite.Group(self.player1, self.player2, self.ball)

        # scores
        self.score1 = 0
        self.score2 = 0

        # match timer (seconds)
        self.match_time = 90
        self.start_ticks = pygame.time.get_ticks()

        # goal areas
        self.goal_left = pygame.Rect(0, 200, 20, 200)
        self.goal_right = pygame.Rect(780, 200, 20, 200)

        self.font = pygame.font.SysFont(None, 48)

    def reset_ball(self):
        self.ball.rect.center = (400, 300)
        self.ball.velocity = [0, 0]

    def check_goal(self):
        if self.goal_left.colliderect(self.ball.rect):
            self.score2 += 1
            self.reset_ball()
        elif self.goal_right.colliderect(self.ball.rect):
            self.score1 += 1
            self.reset_ball()

    def draw_scoreboard(self, time_left):
        score_text = self.font.render(f"{self.score1} - {self.score2}", True, (255, 255, 255))
        time_text = self.font.render(f"{time_left}", True, (255, 255, 0))
        self.screen.blit(score_text, (350, 20))
        self.screen.blit(time_text, (700, 20))

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player1.update(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
            self.player2.update(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
            self.ball.update()

            # collision: kick ball
            if pygame.sprite.collide_rect(self.player1, self.ball):
                self.ball.velocity = [5, 0]
            if pygame.sprite.collide_rect(self.player2, self.ball):
                self.ball.velocity = [-5, 0]

            # check goals
            self.check_goal()

            # calculate time left
            seconds_passed = (pygame.time.get_ticks() - self.start_ticks) // 1000
            time_left = max(0, self.match_time - seconds_passed)

            # end match
            if time_left == 0:
                running = False

            # draw
            self.screen.fill((0, 128, 0))  # green field
            pygame.draw.rect(self.screen, (255, 255, 255), self.goal_left)
            pygame.draw.rect(self.screen, (255, 255, 255), self.goal_right)
            self.all_sprites.draw(self.screen)
            self.draw_scoreboard(time_left)
            pygame.display.flip()

        # show final result
        self.screen.fill((0, 0, 0))
        result = self.font.render(f"Final Score: {self.score1} - {self.score2}", True, (255, 255, 255))
        self.screen.blit(result, (250, 250))
        pygame.display.flip()
        pygame.time.wait(5000)
        pygame.quit()
