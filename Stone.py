import pygame
import pygame.sprite


class Stone(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        for monster in  self.player.game.check_collision(self, self.player.game.all_monster):
            self.player.all_projectil.remove(self)
            monster.damage(self.player.attak)
        if self.rect.x > 1080:
            self.player.all_projectil.remove(self)
