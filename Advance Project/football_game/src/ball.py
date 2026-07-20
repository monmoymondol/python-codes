import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [0, 0]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # friction
        self.velocity[0] *= 0.95
        self.velocity[1] *= 0.95
