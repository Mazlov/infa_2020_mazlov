import pygame
from pygame.draw import *

pygame.init()
COL1=(230,200,175)
FPS = 30
s = pygame.display.set_mode((1000, 800))
s.fill((255,255,255))
circle(s, (255,100,0), (450, 800), 250)
circle(s, COL1, (450, 400), 200)

line(s, COL1, (220,580),(90,130), 30)
line(s, COL1, (680,580),(830,130), 30)
circle(s, COL1, (80, 95), 40)
circle(s, COL1, (840, 95), 40)

circle(s, (130,180,255), (370, 350), 40)
circle(s, (0,0,0), (370, 350), 10)

circle(s, (130,180,255), (530, 350), 40)
circle(s, (0,0,0), (530, 350), 10)

polygon(s, (255,0,0), [(450,540),(330,460), (560, 460)])
polygon(s, (120,70,30), [(450,450),(430,415), (470, 415)])
polygon(s, (255,100,0), [(180,680),(170,580), (255, 530), (315,600), (270,690)])
polygon(s, (255,100,0), [(640,690),(720,660), (720, 570), (640,530), (590,600)])
arc(s,(210,40,255),pygame.Rect(230,180, 440,440),3.14/4, 3*3.14/4, 30 )
rect(s, (0,255,0), (0, 0, 1000, 80))


font = pygame.font.Font(None, 130)
text=font.render('PYTHON is AMAZING', 1, (0,0,0))
s.blit(text, (0,0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
