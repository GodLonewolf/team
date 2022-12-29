import pygame
import os
try:
    os.chdir('games_python\\tictactoe')
except:
    pass

root = pygame.display.set_mode((630, 730))
pygame.init()
postgamefont = pygame.font.Font('assets\\tictactoe_font.ttf', 64)

theme = 'dark'


def main():
    global bg, oimg, ximg, filled, current, theme, bimgs, game
    filled = [' ']
    current = 'o'
    bimgs = [' ',
             'Assets\\{}_blank.png', 'Assets\\{}_blank.png', 'Assets\\{}_blank.png',
             'Assets\\{}_blank.png', 'Assets\\{}_blank.png', 'Assets\\{}_blank.png',
             'Assets\\{}_blank.png', 'Assets\\{}_blank.png', 'Assets\\{}_blank.png', 'Assets\\{}_blank.png']
    game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while True:
        root.fill('#222222')
        bg = pygame.image.load(f'Assets\\{theme}_bg.png')
        oimg = 'Assets\\{}_o.png'
        ximg = 'Assets\\{}_x.png'
        b1 = pygame.Rect(65, 165, 155, 155)
        b2 = pygame.Rect(240, 165, 155, 155)
        b3 = pygame.Rect(415, 165, 155, 155)
        b4 = pygame.Rect(65, 340, 155, 155)
        b5 = pygame.Rect(240, 340, 155, 155)
        b6 = pygame.Rect(415, 340, 155, 155)
        b7 = pygame.Rect(65, 515, 155, 155)
        b8 = pygame.Rect(240, 515, 155, 155)
        b9 = pygame.Rect(415, 515, 155, 155)
        boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and 70 < mouse[0] < 134 and 50 < mouse[1] < 114:
                if theme == 'light':
                    theme = 'dark'
                elif theme == 'dark':
                    theme = 'light'
            elif event.type == pygame.MOUSEBUTTONDOWN and 65 < mouse[0] < 220 and 165 < mouse[1] < 320 and b1 not in filled:
                game[1] = current
                bimgs[1] = set_piece(b1)
            elif event.type == pygame.MOUSEBUTTONDOWN and 240 < mouse[0] < 395 and 165 < mouse[1] < 320 and b2 not in filled:
                game[2] = current
                bimgs[2] = set_piece(b2)
            elif event.type == pygame.MOUSEBUTTONDOWN and 415 < mouse[0] < 570 and 165 < mouse[1] < 320 and b3 not in filled:
                game[3] = current
                bimgs[3] = set_piece(b3)
            elif event.type == pygame.MOUSEBUTTONDOWN and 65 < mouse[0] < 220 and 340 < mouse[1] < 495 and b4 not in filled:
                game[4] = current
                bimgs[4] = set_piece(b4)
            elif event.type == pygame.MOUSEBUTTONDOWN and 240 < mouse[0] < 395 and 340 < mouse[1] < 495 and b5 not in filled:
                game[5] = current
                bimgs[5] = set_piece(b5)
            elif event.type == pygame.MOUSEBUTTONDOWN and 415 < mouse[0] < 570 and 340 < mouse[1] < 495 and b6 not in filled:
                game[6] = current
                bimgs[6] = set_piece(b6)
            elif event.type == pygame.MOUSEBUTTONDOWN and 65 < mouse[0] < 220 and 515 < mouse[1] < 670 and b7 not in filled:
                game[7] = current
                bimgs[7] = set_piece(b7)
            elif event.type == pygame.MOUSEBUTTONDOWN and 240 < mouse[0] < 395 and 515 < mouse[1] < 670 and b8 not in filled:
                game[8] = current
                bimgs[8] = set_piece(b8)
            elif event.type == pygame.MOUSEBUTTONDOWN and 415 < mouse[0] < 570 and 515 < mouse[1] < 670 and b9 not in filled:
                game[9] = current
                bimgs[9] = set_piece(b9)
        if (70 < mouse[0] < 134 and 50 < mouse[1] < 114):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif (65 < mouse[0] < 220 and 165 < mouse[1] < 318 and b1 not in filled) or (240 < mouse[0] < 395 and 165 < mouse[1] < 318 and b2 not in filled) or (415 < mouse[0] < 570 and 165 < mouse[1] < 318 and b3 not in filled):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif (65 < mouse[0] < 220 and 340 < mouse[1] < 495 and b4 not in filled) or (240 < mouse[0] < 395 and 340 < mouse[1] < 495 and b5 not in filled) or (415 < mouse[0] < 570 and 340 < mouse[1] < 495 and b6 not in filled):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif (65 < mouse[0] < 220 and 515 < mouse[1] < 670 and b7 not in filled) or (240 < mouse[0] < 395 and 515 < mouse[1] < 670 and b8 not in filled) or (415 < mouse[0] < 570 and 515 < mouse[1] < 670 and b9 not in filled):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        display(bimgs)
        check_sol()


def display(bimgs):
    root.blit(bg, (0, 0))
    root.blit(pygame.image.load(
        'Assets\\{}_theme.png'.format(theme)), (70, 50))
    root.blit(pygame.image.load(bimgs[1].format(theme)), (65, 165))
    root.blit(pygame.image.load(bimgs[2].format(theme)), (240, 165))
    root.blit(pygame.image.load(bimgs[3].format(theme)), (415, 165))
    root.blit(pygame.image.load(bimgs[4].format(theme)), (65, 340))
    root.blit(pygame.image.load(bimgs[5].format(theme)), (240, 340))
    root.blit(pygame.image.load(bimgs[6].format(theme)), (415, 340))
    root.blit(pygame.image.load(bimgs[7].format(theme)), (65, 515))
    root.blit(pygame.image.load(bimgs[8].format(theme)), (240, 515))
    root.blit(pygame.image.load(bimgs[9].format(theme)), (415, 515))
    pygame.display.update()


def display_postgame():
    root.fill(bg)
    root.blit(pygame.image.load(
        'Assets\\{}_theme.png'.format(theme)), (70, 50))
    pygame.draw.rect(root, finalcolor, final, border_radius=20)
    headfontrender = postgamefont.render(headtext, True, fontcolor)
    headtext_x = (630 - headfontrender.get_size()[0])//2
    root.blit(headfontrender, (headtext_x, 220))
    root.blit(pygame.image.load(
        'Assets\\{}_restart.png'.format(btncolor)), (restart_btn.x, restart_btn.y))
    root.blit(pygame.image.load(
        'Assets\\{}_quit.png'.format(btncolor)), (quit_btn.x, quit_btn.y))
    pygame.display.update()


def set_piece(box_rect):
    global current
    filled.append(box_rect)
    if current == 'o':
        current = 'x'
        return oimg
    if current == 'x':
        current = 'o'
        return ximg


def check_sol():
    if game[1] == game[2] and game[2] == game[3] and game[1] != ' ':
        postgame(game[1])
    elif game[4] == game[5] and game[5] == game[6] and game[4] != ' ':
        postgame(game[4])
    elif game[7] == game[8] and game[8] == game[9] and game[7] != ' ':
        postgame(game[7])
    elif game[1] == game[4] and game[4] == game[7] and game[1] != ' ':
        postgame(game[1])
    elif game[2] == game[5] and game[5] == game[8] and game[2] != ' ':
        postgame(game[2])
    elif game[3] == game[6] and game[6] == game[9] and game[3] != ' ':
        postgame(game[3])
    elif game[1] == game[5] and game[5] == game[9] and game[1] != ' ':
        postgame(game[1])
    elif game[3] == game[5] and game[5] == game[7] and game[3] != ' ':
        postgame(game[3])
    if game[1] != ' ' and game[2] != ' ' and game[3] != ' ' and game[4] != ' ' and game[5] != ' ' and game[6] != ' ' and game[7] != ' ' and game[8] != ' ' and game[9] != ' ':
        postgame('winner')


def postgame(winner):
    global final, theme, final, bg, finalcolor, headtext, fontcolor, restart_btn, quit_btn, btncolor
    final = pygame.Rect(60, 200, 510, 450)
    if winner == 'x':
        headtext = 'X Wins!'
    elif winner == 'o':
        headtext = 'O Wins!'
    else:
        headtext = 'Tied!'

    quit_btn = pygame.Rect(220, 530, 70, 70)
    restart_btn = pygame.Rect(340, 530, 70, 70)
    quithover = 0
    restarthover = 0
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and 70 < mouse[0] < 134 and 50 < mouse[1] < 114:
                if theme == 'light':
                    theme = 'dark'
                elif theme == 'dark':
                    theme = 'light'
            if event.type == pygame.MOUSEBUTTONDOWN and 220 < mouse[0] < 290 and 520 < mouse[1] < 600:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and 340 < mouse[0] < 410 and 520 < mouse[1] < 600:
                main()
        if theme == 'light':
            finalcolor = '#aaaaaa'
            bg = '#cccccc'
            fontcolor = '#222222'
            btncolor = 'dark'
        elif theme == 'dark':
            finalcolor = '#444444'
            bg = '#222222'
            fontcolor = '#cccccc'
            btncolor = 'light'
        if 220 < mouse[0] < 290 and 520 < mouse[1] < 600:
            if quithover < 10:
                quit_btn.y -= 1
                quithover += 1
        else:
            if quithover > 0:
                quit_btn.y += 2
                quithover -= 2
                if quithover < 0:
                    quithover = 0
        if 340 < mouse[0] < 410 and 520 < mouse[1] < 600:
            if restarthover < 10:
                restart_btn.y -= 1
                restarthover += 1
        else:
            if restarthover > 0:
                restart_btn.y += 2
                restarthover -= 2
                if restarthover < 0:
                    restarthover = 0

        if (70 < mouse[0] < 134 and 50 < mouse[1] < 114) or (220 < mouse[0] < 290 and 520 < mouse[1] < 600) or (340 < mouse[0] < 410 and 520 < mouse[1] < 600):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        display_postgame()


main()
