import pygame
from pygame.draw import *
from random import randint

pygame.init()

screen_width = 1200
screen_height = 700
dt = 1
FPS = 120
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.draw.line(screen, (0, 255, 0), (0, 100), (screen_width, 100), 5)
image = pygame.image.load('woo.png').convert_alpha()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:

    def __init__(self, x, y, r, color, vx, vy, alive=True, ball_time=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = vx
        self.vy = vy
        self.alive = alive
        self.ball_time = ball_time

    def update(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r)
        self.x += self.vx * dt
        if self.x + self.r >= screen_width:
            self.x = screen_width - 1 - self.r
            self.vx = -self.vx
        if self.x - self.r <= 0:
            self.x = 1 + self.r
            self.vx = -self.vx
        self.y += self.vy * dt
        if self.y + self.r >= screen_height:
            self.y = screen_height - 1 - self.r
            self.vy = -self.vy
        if self.y - self.r <= 105:
            self.y = 106 + self.r
            self.vy = -self.vy
        self.ball_time += dt
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def live(self, pos):
        s = (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2
        if s <= self.r ** 2:
            self.alive = False

    def kill(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r)

def creation():
    balls.insert(0, Ball(
        randint(100, screen_width - 100),
        randint(205, screen_height - 100),
        randint(30, 100),
        COLORS[randint(0, 5)],
        randint(1, 10),
        randint(1, 10)))


def score_table(string):
    font = pygame.font.Font(None, 100)
    text = font.render("счет: " + string, 1, (255, 0, 0))
    screen.blit(text, (0, 0))


score = 0
balls = []
ball_time = -dt
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:

    miss = True
    clock.tick(FPS)
    ball_time += dt
    new_balls = []
    click = (0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = event.pos

    if ball_time % 180 == 0:
        creation()
        for ball_i in balls:

            if (ball_i.x-balls[0].x)**2 + (ball_i.y-balls[0].y)**2 <= (ball_i.r + balls[0].r)**2 + 2:
                balls.pop(0)
                creation()



    for ball_i in balls:

        for ball_j in balls:
            if (ball_i.x - ball_j.x)**2 + (ball_i.y - ball_j.y)**2 <= (ball_i.r + ball_j.r)**2 and (ball_i != ball_j):
                pygame.draw.circle(screen, BLACK, (ball_i.x, ball_i.y), ball_i.r)
                pygame.draw.circle(screen, BLACK, (ball_j.x, ball_j.y), ball_j.r)
                ball_i.x += ball_j.vx
                ball_j.x += ball_i.vx
                ball_i.y += ball_j.vy
                ball_j.y += ball_i.vy
                ball_i.vx, ball_j.vx, ball_i.vy, ball_j.vy = ball_j.vx, ball_i.vx, ball_j.vy, ball_i.vy

        ball_i.update()

        ball_i.live(click)

        if ball_i.ball_time == 900:
           ball_i.alive = False
           score -= 2

        if ball_i.alive:
            new_balls.append(ball_i)
        else:
            ball_i.kill()
            score += 1

    balls = new_balls

    pygame.draw.circle(screen, BLACK, (210, 10), 90)
    score_table(str(score))
    pygame.draw.line(screen, (0, 255, 0), (0, 100), (screen_width, 100), 5)
    #screen.blit(image, (500, 300))

    pygame.display.update()

pygame.quit()
