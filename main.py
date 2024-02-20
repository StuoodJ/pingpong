# Example file showing a basic pygame "game loop"
import pygame
import random
# pygame setup
pygame.init()
dW = 600
dH = 500
screen = pygame.display.set_mode((dW, dH))
clock = pygame.time.Clock()
running = True
dt = 0
#/ VARIABLES
text_font = pygame.font.SysFont(None, 30)
bW = 25
bH = 75
blx = 50
bly = (dH/2)-(bH/2)
brx = (dW-bW)-(bW*2)
bry = (dH/2)-(bH/2)
ballr = 10
ballpos = pygame.Vector2(dW/2+0, dH/2)
left = 0
right = 1
blocklscore = 0
blockrscore = 0
hitbottom = 0
from text import drawtext as txt
#/ GAME RUNNING
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    #/ CONTROLS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bly -= 350 * dt
    if keys[pygame.K_s]:
        bly += 350 * dt
    if keys[pygame.K_UP]:
        bry -= 350 * dt
    if keys[pygame.K_DOWN]:
        bry += 350 * dt
    if bly+bH >= dH:
        bly = dH-bH
    if bly <= 0:
        bly = 0
    if bry+bH >= dH:
        bry = dH-bH
    if bry <= 0:
        bry = 0
    #/BALL MOVEMENT
    if right == 1:
        if not ballpos.x >= brx:
            if not hitbottom == 1:
                ballpos.y += (100)*dt
            else:
                ballpos.y -= (100)*dt
            ballpos.x += 175*dt
        else:
            if bry+bH >= ballpos.y and bry <= ballpos.y:
                right = 0
                left = 1
            else:
                ballpos = pygame.Vector2(dW/2,dH/2)
                blocklscore += 1
    if left == 1:
        if not ballpos.x <= blx+bW:
            if not hitbottom == 1:
                ballpos.y += (random.randrange(-1, 1)*100)*dt
            else:
                ballpos.y -= (100)*dt
            ballpos.x -= 175*dt
        else:
            if bly+bH >= ballpos.y and bly <= ballpos.y:
                left = 0
                right = 1
            else:
                ballpos = pygame.Vector2(dW/2,dH/2)
                blockrscore += 1
    if ballpos.y >= dH:
        hitbottom = 1
        ballpos.y -= 1000 * dt
        if left == 1:
            ballpos.x -= 175*dt
        elif right == 1:
            ballpos.x += 175*dt
    elif ballpos.y <= dH/2:
        hitbottom = 0
    if ballpos.y <= 0:
        ballpos.y += 1000 * dt
        if left == 1:
            ballpos.x -= 175*dt
        elif right == 1:
            ballpos.x += 175*dt
    #/ RENDER
    txt(screen, str(blocklscore), text_font, (255, 255, 255), blx-25, 25)
    txt(screen, str(blockrscore), text_font, (255, 255, 255), brx+25, 25)
    blocklrect = pygame.Rect(blx, bly, bW, bH)
    blockrrect = pygame.Rect(brx, bry, bW, bH)
    ball = pygame.draw.circle(screen, (255,255,255), ballpos, ballr)
    blockl = pygame.draw.rect(screen, (255,255,255), blocklrect)
    blockr = pygame.draw.rect(screen, (255,255,255), blockrrect)
    #/ SCREEN
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()