import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя первая игра")
icon = pygame.image.load("image/1337497_game_go_play_pikachu_pokemon_icon.png")
pygame.display.set_icon(icon)

square = pygame.Surface((10, 10))
square.fill('Yellow')

#myfont = pygame.font.Font('')

running = True
while running:

    pygame.draw.circle(square, 'Red', (10, 10), 10)

    screen.blit(square, (10, 0))

    pygame.display.update()

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
            pygame.quit()





