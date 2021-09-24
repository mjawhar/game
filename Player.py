import pygame

from Stone import Stone


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHelth = 100
        self.attak = 10
        self.velocity = 5
        self.all_projectil = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def lunch(self):
        stone = Stone(self)
        self.all_projectil.add(stone)
