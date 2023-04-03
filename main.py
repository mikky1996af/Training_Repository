import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("Моя первая игра")
icon = pygame.image.load("image/1337497_game_go_play_pikachu_pokemon_icon.png")
pygame.display.set_icon(icon)

bg = pygame.image.load('image/gamingBackground-1024x576.png')
walk_right = [
    pygame.image.load('image/player_right/game-animation-1.png'),
    pygame.image.load('image/player_right/game-animation-2.png'),
    pygame.image.load('image/player_right/game-animation-3.png'),
    pygame.image.load('image/player_right/game-animation-4.png'),
]
walk_left = [
    pygame.image.load('image/player_left/game-animation-1.png'),
    pygame.image.load('image/player_left/game-animation-2.png'),
    pygame.image.load('image/player_left/game-animation-3.png'),
    pygame.image.load('image/player_left/game-animation-4.png'),
]

player_anim_count = 0
bg_x = 0
player_speed = 5
player_x = 150

bg_sound = pygame.mixer.Sound('sounds/Wiz_Khalifa_Ty_Dolla_ign_Sueco_the_Child_Lil_Yachty_-_Speed_Me_Up_From_Sonic_the_Hedgehog_68236432.mp3')
bg_sound.play()

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1024, 0))
    keys = pygame.key.get_pressed()
    if  keys[pygame.K_LEFT]:
         screen.blit(walk_left[player_anim_count], (player_x, 50))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, 50))

    if keys[pygame.K_LEFT] and player_x > -450:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 150:
        player_x += player_speed

    if player_anim_count == len(walk_right) - 1:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -1024:
        bg_x = 0


    pygame.display.update()

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
            pygame.quit()


    clock.tick(15)



