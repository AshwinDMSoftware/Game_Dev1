# Example file showing a circle moving on screen
import pygame
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos1 = pygame.Vector2(50, screen.get_height() / 2)
player_pos2 = pygame.Vector2(screen.get_width()-50, screen.get_height() / 2)
ball_pos =pygame.Vector2(screen.get_width()/2, screen.get_height() / 2)
ball_speed_x = 3
ball_speed_y = 3
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, "blue", (player_pos1.x,player_pos1.y,5,60))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos1.y> 0:
        player_pos1.y -= 300 * dt
    if keys[pygame.K_s] and player_pos1.y<screen.get_height()-50:
        player_pos1.y += 300 * dt

    pygame.draw.rect(screen, "red", (player_pos2.x,player_pos2.y,5,60))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos2.y> 0:
        player_pos2.y -= 300 * dt
    if keys[pygame.K_DOWN] and player_pos2.y<screen.get_height()-50:
        player_pos2.y += 300 * dt


    ball_pos.x += ball_speed_x
    ball_pos.y += ball_speed_y
    if ball_pos.y < 0 or ball_pos.y > screen.get_height():
        #ball_speed_x= -ball_speed_x
        ball_speed_y = -ball_speed_y
    if ball_pos.x > screen.get_width():
        ball_pos =pygame.Vector2(screen.get_width()/2, screen.get_height() / 2)

    if player_pos2.y -10 > ball_pos.y > player_pos2.y +10:
        if player_pos2.x -10 > ball_pos.x > player_pos2.x +10:
            ball_speed_x= -ball_speed_x
            ball_speed_y = -ball_speed_y
    pygame.draw.circle(screen, "black",ball_pos,10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
#Test\
#Test 2
pygame.quit()