import pygame


class Monstre(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHelth = 100
        self.attak = 10
        self.velocity = 1
        self.all_projectil = pygame.sprite.Group()
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            self.rect.x = 1000

    def forward(self, game):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity

    # def update_health(self):
    #     bar_color = (111, 210, 46)
    #     bar_position =
