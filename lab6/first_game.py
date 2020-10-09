import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x, y, r = 0, 0, 0

def new_ball():
    '''рисует новый шарик '''
    global x, y, r, color, v_x, v_y
    x = randint(100, 1100)
    y = randint(100, 600)
    r = randint(10, 100)
    v_x = randint(-5, 5)
    v_y = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def scoretable(string):
    font = pygame.font.Font(None, 100)
    text = font.render(string, 1, (255, 0, 0))
    screen.blit(text, (0, 0))

score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (mouse_x - x)**2 + (mouse_y - y)**2 <= r**2:
                score += 1
            else:
                score -= 1
            new_ball()
    x += v_x
    y += v_y
    if (x - r <= 0) or (x + r >=1200):
        v_x = -v_x
    if (y - r <= 0) or (y + r >= 700):
        v_y = -v_y
    circle(screen, color, (x, y), r)
    scoretable(str(score))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()