import pygame
pygame.init()
win_width = 1100
win_height = 800
root = pygame.display.set_mode((win_width, win_height))


def display():
    root.fill('#222222')
    pygame.draw.rect(root, '#ffffff', player1, border_radius=12)
    pygame.draw.rect(root, '#ffffff', player2, border_radius=12)
    pygame.display.update()


def main():
    global player1, player2
    clock = pygame.time.Clock()
    FPS = 60
    block_width = 12
    block_height = 125
    player1 = pygame.Rect(10, 10, block_width, block_height)
    player2 = pygame.Rect(win_width - 22, 10, block_width, block_height)
    while True:
        clock.tick(FPS)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.y > 10:
            player1.y -= 7
        if keys[pygame.K_s] and player1.y < win_height - player1.height:
            player1.y += 7
        if keys[pygame.K_UP] and player2.y > 10:
            player2.y -= 7
        if keys[pygame.K_DOWN] and player2.y < win_height - player2.height:
            player2.y += 7

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        display()


main()
