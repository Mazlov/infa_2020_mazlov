import pygame
from pygame.draw import *
from random import randint
pygame.init()

screen_width = 1200
screen_height = 700
dt = 1
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.draw.line(screen, (0, 255, 0), (0, 100), (screen_width, 100), 5)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball():

    def __init__(self, x, y, r, color, vx, vy, alive=True, time=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = vx
        self.vy = vy
        self.alive = alive
        self.time = time

    def update(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r)
        self.x += self.vx * dt
        if (self.x + self.r >= screen_width):
            self.x = screen_width - 1 - self.r
            self.vx = -self.vx
        if (self.x - self.r <= 0):
            self.x = 1 + self.r
            self.vx = -self.vx
        self.y += self.vy * dt
        if (self.y + self.r >= screen_height):
            self.y = screen_height - 1 - self.r
            self.vy = -self.vy
        if (self.y - self.r <= 105):
            self.y = 106 + self.r
            self.vy = -self.vy
        self.time += dt
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def live (self, pos):
        s = (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2
        if (s <= self.r ** 2):
            self.alive = False

    def kill (self):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r)

def scoretable(string):
    font = pygame.font.Font(None, 100)
    text = font.render(string, 1, (255, 0, 0))
    screen.blit(text, (0, 0))

score = 0
balls = []
time = -dt
pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:

    miss = True
    clock.tick(FPS)
    time += dt
    new_balls = []
    click = (0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = event.pos

    if (time % 180 == 0):
        balls.append( Ball(
                        randint(100, screen_width - 100),
                        randint(205, screen_height - 100),
                        randint(30,100),
                        COLORS[randint(0, 5)],
                        randint(1,10),
                        randint(1,10),
                        True,
                        0
                        ))

    for ball_i in balls:
        ball_i.update()
        ball_i.live(click)
        if ball_i.time == 600:
            ball_i.alive = False
            score -= 1
        if (ball_i.alive == True):
            new_balls.append(ball_i)
        else:
            ball_i.kill()
            score += 1

    balls = new_balls


    pygame.draw.circle(screen, BLACK, (10, 10), 70)
    scoretable(str(score))

    pygame.display.update()

pygame.quit()