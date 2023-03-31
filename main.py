import pygame

pygame.init()
screen = pygame.display.set_mode((750, 422))
pygame.display.set_caption("Моя первая игра")
icon = pygame.image.load("image/1337497_game_go_play_pikachu_pokemon_icon.png")
pygame.display.set_icon(icon)

bg = pygame.image.load('image/1645170427_9-phonoteka-org-p-zadnii-fon-iz-igr-9.png')


running = True
while running:

    screen.blit(bg, (0, 0))
    pygame.display.update()

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
            pygame.quit()





