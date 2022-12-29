import pygame
from math import *
win_width, win_height = 1000, 1000
root = pygame.display.set_mode((win_width, win_height))
pygame.init()


def display():
    root.fill('#222222')
    pygame.draw.rect(root, '#cccccc', planet, border_radius=planet.width//2)
    pygame.draw.rect(root, '#cccccc', ufo, border_radius=25)
    pygame.display.flip()


def main():
    global planet, ufo
    planet_radius = 300
    angle = 0
    x, y = 325, 325
    ufo = pygame.Rect(x, y, 50, 50)

    planet = pygame.Rect((win_width - planet_radius)//2,
                         (win_height - planet_radius)//2, planet_radius, planet_radius)

    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ufo.x = x*cos(angle)+475
        ufo.y = -y*sin(angle)+475
        if keys[pygame.K_LEFT]:
            angle += 0.0035
        if keys[pygame.K_RIGHT]:
            angle -= 0.0035
        display()


main()
