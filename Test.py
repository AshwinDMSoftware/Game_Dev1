import pygame
import time
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
ball_base = 3
player_speed = 300
base_player_speed = 300
#Player scores
score1 = 0
score2 = 0
#Score Text setup
font = pygame.font.Font('freesansbold.ttf', 32)
#Player 1 Score
score1_display = font.render(str(score1),True, 'green','blue')
score1_displayRect = score1_display.get_rect()
score1_displayRect.center = (1280 // 4, 30)
#Player 2 Score
score2_display = font.render(str(score2),True, 'green','blue')
score2_displayRect = score1_display.get_rect()
score2_displayRect.center = (1280*3//4, 30)
#End Score Display
scoreFinal_display = font.render("Not Decided",True, 'green','blue')
scoreFinal_displayRect = scoreFinal_display.get_rect()
scoreFinal_displayRect.center = (1280//2, 720//2)

#Some functions that can affect gameplay
def paddleSpeed():
    global player_speed
    if player_speed == base_player_speed:
        player_speed = player_speed*2
def removePaddleSpeed():
    global  player_speed
    if player_speed != base_player_speed:
        player_speed = base_player_speed
def ballSpeed():
    global ball_speed_x
    global ball_speed_y
    if abs(ball_speed_x) == ball_base:
        ball_speed_x = ball_speed_x*2
        ball_speed_y = ball_speed_y*2
def removeBallSpeed():
    global ball_speed_x
    global ball_speed_y
    if abs(ball_speed_x) != ball_base:
        if ball_speed_x <0:
            ball_speed_x = -ball_base
        else:
            ball_speed_x = ball_base
        if ball_speed_y < 0:
            ball_speed_y = -ball_base
        else:
            ball_speed_y = ball_base
def freezeBall():
    global ball_speed_x
    global ball_speed_y
    ball_speed_x = 0
    ball_speed_y = 0
def switchBall():
    global ball_speed_x
    global ball_speed_y
    ball_speed_x = -ball_speed_x
    ball_speed_y = -ball_speed_y
def reversePlayer():
    global player_speed
    if player_speed == base_player_speed:
        player_speed = -player_speed
startTime = int(time.time())
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    #Basic text display
    score1_display = font.render(str(score1), True, 'green', 'blue')
    score2_display = font.render(str(score2), True, 'green', 'blue')
    screen.blit(score1_display, score1_displayRect)
    screen.blit(score2_display, score2_displayRect)
    player_1 = pygame.Rect((player_pos1.x,player_pos1.y,5,60))
    pygame.draw.rect(screen, "blue", player_1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos1.y> 0:
        player_pos1.y -= player_speed * dt
    if keys[pygame.K_s] and player_pos1.y<screen.get_height()-50:
        player_pos1.y += player_speed * dt
    player_2 = pygame.Rect((player_pos2.x, player_pos2.y, 5, 60))
    pygame.draw.rect(screen, "red", player_2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos2.y> 0:
        player_pos2.y -= player_speed * dt
    if keys[pygame.K_DOWN] and player_pos2.y<screen.get_height()-50:
        player_pos2.y += player_speed * dt


    ball_pos.x += ball_speed_x
    ball_pos.y += ball_speed_y
    #If ball hits bottom or top wall
    if ball_pos.y < 0 or ball_pos.y > screen.get_height():
        ball_speed_y = -ball_speed_y
    #If ball hits right wall
    if ball_pos.x > screen.get_width():
        ball_pos =pygame.Vector2(screen.get_width()/2, screen.get_height() / 2)
        score1+= 1
    #If ball hits left wall
    if ball_pos.x < 0:
        ball_pos =pygame.Vector2(screen.get_width()/2, screen.get_height() / 2)
        score2+= 1
    #Player collision
    player1_hit = player_1.collidepoint(ball_pos)
    player2_hit = player_2.collidepoint(ball_pos)
    if player1_hit or player2_hit:
        ball_speed_x = -ball_speed_x
    #Random Events
    currentTime = int(time.time())-startTime
    if currentTime > 5:
        reversePlayer()
        if currentTime > 10:
            removePaddleSpeed()
            startTime = int(time.time())
    #End State
    if score1 > 4:
        scoreFinal_display = font.render("PLAYER 1 WINS!!!",True, 'green','blue')
        screen.blit(scoreFinal_display, scoreFinal_displayRect)
    if score2 > 4:
        scoreFinal_display = font.render("PLAYER 2 WINS!!!", True, 'green', 'blue')
        screen.blit(scoreFinal_display, scoreFinal_displayRect)
    pygame.draw.circle(screen, "black",ball_pos,10)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    print(currentTime)
pygame.quit()