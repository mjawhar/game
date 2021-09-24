import pygame
from Game import Game

pygame.init()

pygame.display.set_caption("test");
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load("assets/bg.jpg")
running = True
game = Game()

while running:

    for stone in game.player.all_projectil:
        stone.move()

    for monster in game.all_monster:
        monster.forward(game)

    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)
    game.player.all_projectil.draw(screen)
    game.all_monster.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_DOWN:
                game.player.lunch()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

