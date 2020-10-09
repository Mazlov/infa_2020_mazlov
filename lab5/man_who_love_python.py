import pygame
from pygame.draw import *


def eye(x, y, color, size):
    circle(s, color, (x, y), int(0.4 * size))
    circle(s, (0, 0, 0), (x, y), int(0.1 * size))


def hands(color, size, x_right_arm, y_right_arm, x_left_arm, y_left_arm):
    line(s, color, (x_left_arm + int(1.4 * size), y_left_arm + int(4.85 * size)),
         (x_left_arm + int(0.1 * size), y_left_arm + int(0.35 * size)), int(0.3 * size))
    line(s, color, (x_right_arm - int(1.6 * size), y_right_arm + int(4.85 * size)),
         (x_right_arm - int(0.1 * size), y_right_arm + int(0.35 * size)), int(0.3 * size))
    circle(s, color, (x_left_arm, y_left_arm), int(0.4 * size))
    circle(s, color, (x_right_arm, y_right_arm), int(0.4 * size))


def head(color, x_r, x_l, y_r, y_l, size):
    circle(s, color, (int((x_r + x_l) / 2), int((y_r + y_l) / 2 + 0.5 * size)),
           int(2 * size))


def body(color, x, y, size):
    circle(s, color, (x, y), int(2.5 * size))
    polygon(s, color, [(x - int(2.7 * size), y - int(1.2 * size)), (x - int(2.7 * size), y - int(2.2 * size)),
                       (x - int(1.95 * size), y - int(2.7 * size)), (x - int(1.35 * size), y - int(2 * size)),
                       (x - int(1.8 * size), y - int(1.1 * size))])
    polygon(s, color, [(x + int(1.9 * size), y - int(1.1 * size)), (x + int(2.7 * size), y - int(1.4 * size)),
                       (x + int(2.7 * size), y - int(2.3 * size)), (x + int(1.9 * size), y - int(2.7 * size)),
                       (x + int(1.5 * size), y - int(2 * size))])


def mouth(color, x, y, size):
    polygon(s, color, [(x, y - int(2.6 * size)), (x - int(1.2 * size), y - int(3.4 * size)),
                       (x + int(1.2 * size), y - int(3.4 * size))])


def nose(color, x, y, size):
    polygon(s, color, [(x, y - int(3.5 * size)), (x - int(0.2 * size), y - int(3.85 * size)),
                       (x + int(0.2 * size), y - int(3.85 * size))])


def hair(color, size, x, y):
    arc(s, color, pygame.Rect(x - int(1.4 * size), y - int(1.7 * size), int(4.4 * size), int(4.4 * size)), 3.14 / 4,
        3 * 3.14 / 4, int(0.3 * size))


def text_on(string):
    rect(s, (0, 255, 0), (0, 0, 1100, 90))
    font = pygame.font.Font(None, 100)
    text = font.render(string, 1, (0, 0, 0))
    s.blit(text, (0, 0))


pygame.init()

size = 100
x_body = 450
y_body = 800

purple = (210, 40, 255)
brown = (120, 70, 30)
red = (255, 0, 0)
orange = (255, 100, 0)
beige = (230, 200, 175)
blue = (130, 180, 255)
x_left_arm = 80
y_right_arm = y_left_arm = 95
x_right_arm = 820
x_right_eye = 530
x_left_eye = 370
y_left_eye = y_right_eye = 350

FPS = 30
s = pygame.display.set_mode((1100, 800))
pygame.display.set_caption("the man who love python")
s.fill((255, 255, 255))

head(beige, x_right_eye, x_left_eye, y_right_eye, y_left_eye, size)
eye(x_left_eye, y_left_eye, blue, size)
eye(x_right_eye, y_right_eye, blue, size)
hands(beige, size, x_right_arm, y_right_arm, x_left_arm, y_left_arm)
body(orange, x_body, y_body, size)
mouth(red, x_body, y_body, size)
nose(brown, x_body, y_body, size)
hair(purple, size, x_left_eye, y_left_eye)
rect(s, (0, 255, 0), (0, 0, 1000, 80))

clock = pygame.time.Clock()
finished = False
string = '...'

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        string = 'python is amazing'
    if keys[pygame.K_RIGHT]:
        string = 'i love python'
    if keys[pygame.K_UP]:
        string = 'yes, i am crazy about python'
    if keys[pygame.K_DOWN]:
        string = 'python is cool'
    text_on(string)
    pygame.display.update()
pygame.quit()
