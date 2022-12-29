import pygame
import os
import random
try:
    os.chdir('games_python\\flappy_bird')
except:
    pass
pygame.init()
pygame.font.init()
images = ['Assets\\bird1.png', 'Assets\\bird2.png', 'Assets\\bird3.png']
root = pygame.display.set_mode((500, 750))
bg = pygame.image.load('Assets\\bg.png')
pipe1 = pygame.image.load('Assets\\pipe.png')
pipe2 = pygame.image.load('Assets\\pipe.png')
pipe3 = pygame.image.load('Assets\\pipe.png')
ground = pygame.image.load('Assets\\ground.png')
bwidth = bheight = 50
pwidth, pheight = 96, 1216
flappyfont = pygame.font.Font('Assets\\flappy_font.ttf', 50)
postgamefont = pygame.font.Font('Assets\\flappy_font.ttf', 70)


def display_pause():
    pygame.draw.rect(root, '#ffcc00', pygame.Rect(50, 200, 50, 50))
    pygame.display.update()


def display(bird, birdrect, pipe1rectup, pipe2rectup, pipe3rectup, groundrect, score, scorerect, x, font):
    global scoretext
    root.blit(bg, (0, 0))
    root.blit(pipe1, (pipe1rectup.x, pipe1rectup.y))
    root.blit(pipe2, (pipe2rectup.x, pipe2rectup.y))
    root.blit(pipe3, (pipe3rectup.x, pipe3rectup.y))
    root.blit(bird, (birdrect.x, birdrect.y))
    root.blit(ground, (groundrect.x, 0))
    scoretext = font.render(str(score), True, (0, 0, 0))
    root.blit(scoretext, (scorerect.x, scorerect.y))
    pygame.display.update()


def display_pregame(bird, birdrect):
    root.blit(bg, (0, 0))
    root.blit(bird, (birdrect.x, birdrect.y))
    scoretext = flappyfont.render(highscore, True, (0, 0, 0))
    root.blit(scoretext, (40, 40))
    pygame.display.update()


def pregame():
    global pregamepos, highscore
    highscore = open('Assets\\highscore.txt').readline()
    run = True
    i = 0
    v = 1
    clock = pygame.time.Clock()
    birdrect = pygame.Rect(150, 375, bwidth, bheight)
    while run:
        clock.tick(120)
        if birdrect.y > 390:
            v = v*-1
            birdrect.y += v
        if birdrect.y < 360:
            v = v*-1
            birdrect.y += v
        if birdrect.y <= 390 and birdrect.y >= 360:
            birdrect.y += v
        i += 0.75
        if i >= 20:
            i = 0
        if i >= 0 and i < 5:
            bird = pygame.image.load(images[0])
        if (i >= 5 and i < 10) or (i >= 15 and i < 20):
            bird = pygame.image.load(images[1])
        if i >= 10 and i < 15:
            bird = pygame.image.load(images[2])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        pregamepos = birdrect.y
        display_pregame(bird, birdrect)


def main():
    global birdrect, pipe1rectup, pipe2rectup, pipe3rectup, score, scorerect, lastimg, groundrect, scorebg
    keypressed = False
    gravity = 1.3
    velocity = 0
    lift = 30
    score = 0
    speedmultiplier = 0
    i = 0
    pause = False
    birdrect = pygame.Rect(150, pregamepos, bwidth, bheight)
    scorerect = pygame.Rect(40, 40, 1, 1)
    pipe1_random_y = random.randint(-400, -100)
    pipe2_random_y = random.randint(-400, -100)
    pipe3_random_y = random.randint(-400, -100)
    groundrect = pygame.Rect(0, 622, 500, 128)
    scorebg = pygame.Rect((500//2)-10, 323, 20, 84)
    pipe1rectup = pygame.Rect(900, pipe1_random_y, pwidth-20, (pheight-176)//2)
    pipe2rectup = pygame.Rect(1200, pipe2_random_y,
                              pwidth-20, (pheight-176)//2)
    pipe3rectup = pygame.Rect(1500, pipe3_random_y,
                              pwidth-20, (pheight-176)//2)
    pipe1rectdown = pygame.Rect(
        900, pipe1rectup.y + 520 + 176, pwidth-20, (pheight-176)//2)
    pipe2rectdown = pygame.Rect(
        1200, pipe2rectup.y + 520 + 176, pwidth-20, (pheight-176)//2)
    pipe3rectdown = pygame.Rect(
        1500, pipe3rectup.y + 520 + 176, pwidth-20, (pheight-176)//2)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        if pause == True:
            display_pause()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pause = False
        else:
            i += 0.5
            if i == 20:
                i = 0
            if i >= 0 and i < 5:
                bird = pygame.transform.rotate(
                    pygame.image.load(images[0]), -velocity*1.5)
                lastimg = 0
            if (i >= 5 and i < 10) or (i >= 15 and i < 20):
                bird = pygame.transform.rotate(
                    pygame.image.load(images[1]), -velocity*1.5)
                lastimg = 1
            if i >= 10 and i < 15:
                bird = pygame.transform.rotate(
                    pygame.image.load(images[2]), -velocity*1.5)
                lastimg = 2
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        keypressed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    keypressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pause = True
            if score % 25 == 0:
                speedmultiplier = score//25
            pipe1rectup.x -= 3+speedmultiplier
            pipe2rectup.x -= 3+speedmultiplier
            pipe3rectup.x -= 3+speedmultiplier
            pipe1rectdown.x -= 3+speedmultiplier
            pipe2rectdown.x -= 3+speedmultiplier
            pipe3rectdown.x -= 3+speedmultiplier
            if (pipe1rectup.x <= 54 and pipe1rectup.x > 51-speedmultiplier) or (pipe2rectup.x <= 54 and pipe2rectup.x > 51-speedmultiplier) or (pipe3rectup.x <= 54 and pipe3rectup.x > 51-speedmultiplier):
                score += 1
            if pipe1rectup.x < -100:
                pipe1rectup.x = 800
                pipe1rectdown.x = 800
            if pipe2rectup.x < -100:
                pipe2rectup.x = 800
                pipe2rectdown.x = 800
            if pipe3rectup.x < -100:
                pipe3rectup.x = 800
                pipe3rectdown.x = 800
            if groundrect.x < -515:
                groundreset_adjustx = 516 + groundrect.x
                groundrect.x = 0 + groundreset_adjustx

            if keypressed:
                velocity -= lift
                keypressed = False
            else:
                birdrect.y += velocity
                velocity *= 0.9
                velocity += gravity

            groundrect.x -= 3 + speedmultiplier
            display(bird, birdrect, pipe1rectup, pipe2rectup, pipe3rectup,
                    groundrect, score, scorerect, False, flappyfont)
            scorebg = pygame.Rect(
                ((500-scoretext.get_size()[0])//2)-10, 333, scoretext.get_size()[0]+15, 84)
            if birdrect.colliderect(pipe1rectup) or birdrect.colliderect(pipe1rectdown):
                postgame()
            if birdrect.colliderect(pipe2rectup) or birdrect.colliderect(pipe2rectdown):
                postgame()
            if birdrect.colliderect(pipe3rectup) or birdrect.colliderect(pipe3rectdown):
                postgame()
            if birdrect.y >= 560:
                postgame()
            if birdrect.y < -400:
                postgame()


def postgame():
    if int(highscore) < int(score):
        file = open('Assets\\highscore.txt', 'w')
        file.write(str(score))
        file.close()
    postgame = True
    keytimer = 0
    clock = pygame.time.Clock()
    while postgame:
        clock.tick(100)
        keytimer += 1
        bird = pygame.transform.rotate(pygame.image.load(images[lastimg]), -75)
        if birdrect.y < 570:
            birdrect.y += 5
        scorerect.x = (500 - scoretext.get_size()[0])//2
        scorerect.y = 343
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and keytimer > 100:
                    pregame()
            if event.type == pygame.MOUSEBUTTONUP and keytimer > 100:
                pregame()
        display(bird, birdrect, pipe1rectup, pipe2rectup, pipe3rectup,
                groundrect, score, scorerect, True, postgamefont)


pregame()
