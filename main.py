import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("Моя первая игра")
icon = pygame.image.load("image/1337497_game_go_play_pikachu_pokemon_icon.png")
pygame.display.set_icon(icon)

bg = pygame.image.load('image/gamingBackground-1024x576.png')
walk_right = [
    pygame.image.load('image/player_right/game-animation-1.png'),
    pygame.image.load('image/player_right/game-animation-2.png'),
]

walk_left = []

player_anim_count = 0
running = True
while running:

    screen.blit(bg, (0, 0))
    screen.blit(walk_right[player_anim_count], (0, 50))
    if player_anim_count == len(walk_right) - 1:
        player_anim_count = 0
    else:
        player_anim_count += 1


    pygame.display.update()

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
            pygame.quit()





