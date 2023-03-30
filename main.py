import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя первая игра")
icon = pygame.image.load("image/1337497_game_go_play_pikachu_pokemon_icon.png")
pygame.display.set_icon(icon)

running = True
while running:

   # screen.fill((255, 215, 0))

    pygame.display.update()

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_a:
                screen.fill((0, 191, 255))




