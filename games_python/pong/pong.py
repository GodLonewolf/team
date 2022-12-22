import pygame
pygame.init()
win_width = 1100
win_height = 700
root = pygame.display.set_mode((win_width, win_height))


def display():
    root.fill(bg)
    pygame.draw.rect(root, fg, player1, border_radius=3)
    pygame.draw.rect(root, fg, player2, border_radius=3)
    pygame.draw.rect(root, fg, ball, border_radius=10)
    pygame.draw.rect(root, fg, themerect, border_radius=10)
    pygame.draw.rect(root, fg, seperator)
    pygame.display.update()


def reset_score():
    global p1_score, p2_score
    p1_score = 0
    p2_score = 0


def main():
    global player1, player2, ball, fg, bg, themerect, seperator, p1_score, p2_score
    theme = 'dark'
    fg = '#cccccc'
    bg = '#222222'
    FPS = 60
    clock = pygame.time.Clock()
    block_width = 12
    block_height = 140
    ball_radius = 20
    MAX_VEL = 5
    ball_velocity_x = 5
    ball_velocity_y = 5
    player1 = pygame.Rect(10, 110, block_width, block_height)
    player2 = pygame.Rect(win_width - 22, 110, block_width, block_height)
    ball = pygame.Rect(win_width / 2 - 10, win_height /
                       2 - 10, ball_radius, ball_radius)
    themerect = pygame.Rect(19, 19, 64, 64)
    seperator = pygame.Rect(0, 98, win_width, 2)
    gameover = False
    while not gameover:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        if p1_score == 10:
            postgame('Player 1')
        if p2_score == 10:
            postgame('Player 2')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.y > 110:
            player1.y -= 7
        if keys[pygame.K_s] and player1.y < win_height - player1.height - 10:
            player1.y += 7
        if keys[pygame.K_UP] and player2.y > 110:
            player2.y -= 7
        if keys[pygame.K_DOWN] and player2.y < win_height - player2.height - 10:
            player2.y += 7

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        ball.x += ball_velocity_x
        ball.y += ball_velocity_y

        if ball.y <= 100:
            ball.y += 10
            ball_velocity_y *= -1
        if ball.y >= win_height - ball.height:
            ball.y = win_height - ball.height
            ball_velocity_y *= -1
        if ball.colliderect(player1):
            ball_velocity_x *= -1
            middle_y = player1.y + player1.height / 2
            difference_in_y = middle_y - ball.y
            reduction_factor = (block_height / 2) / MAX_VEL
            velocity_y = difference_in_y / reduction_factor
            ball_velocity_y = -velocity_y
        if ball.colliderect(player2):
            ball_velocity_x *= -1
            middle_y = player2.y + player2.height / 2
            difference_in_y = middle_y - ball.y
            reduction_factor = (block_height / 2) / MAX_VEL
            velocity_y = difference_in_y / reduction_factor
            ball_velocity_y = -velocity_y

        if ball.x <= 0:
            p1_score += 1
            main()
        if ball.x >= win_width - ball.width:
            p2_score += 1
            main()

        if (19 < mouse[0] < 83 and 19 < mouse[1] < 83):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        display()


def postgame(winner):
    print(winner)


reset_score()
main()
