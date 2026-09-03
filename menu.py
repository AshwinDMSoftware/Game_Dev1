import pygame
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
#Text setup
font = pygame.font.Font('freesansbold.ttf', 32)
#Start Game Button
start_game = font.render('Start Game',True, 'green','blue')
start_gameRect = start_game.get_rect()
start_gameRect.center = (1280 // 2, 720 // 2)
game_starting = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    screen.blit(start_game, start_gameRect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_gameRect.collidepoint(pygame.mouse.get_pos()):
            game_starting = True
            running = False

    pygame.display.flip()
    dt = clock.tick(60) / 1000
if game_starting:
    with open("Test.py") as file:
        exec(file.read())