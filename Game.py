import pygame

from Monstre import Monstre
from Player import Player


class Game:
    def __init__(self):
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {
        }
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monstre(self)
        self.all_monster.add(monster)
