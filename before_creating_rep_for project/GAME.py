import pygame
import sys
import pygame.draw
import math

FPS = 60

screen_width = 1000
screen_height = 850
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
black = (0, 0, 0)
white = (255, 255, 255)
color_of_doors = (178, 34, 34)
hero_size = {'x': 10, 'y': 10}
hero_x, hero_y = screen_width / 2, screen_height / 2
hero_velocity = 350
mouse_pos = {'x': screen_width / 2, 'y': screen_height / 2}
mouse_impact = 0.2


class all_map():
    def __init__(self, objects):
        """ Конструктор класса all_map
        придает всем объектам нна карте класс all_map, чтобы их можно
        было все одновременно двигать, не двигая персоннажа
        Args:
        objects - объект класса all_map
        """
        self.objects = objects
        self.color = black

    def render(self):
        screen.fill(white)
        for object in self.objects:
            object.draw()

    def forward(self, axis_x, axis_y):
        # функция движения всей карты вперед
        t = True
        for object in self.objects:
            t = t and not (object.x - mouse_pos['x'] * mouse_impact + object.width >= hero_x and object.x - mouse_pos[
                'x'] * mouse_impact <= hero_x and object.y - mouse_pos[
                               'y'] * mouse_impact + object.height * 0.4 >= hero_y and object.y - mouse_pos[
                               'y'] * mouse_impact <= hero_y + 9)
        for object in self.objects:
            if t:
                if axis_y == 1:
                    object.y -= hero_velocity / FPS / (2 ** 0.5)
                else:
                    object.y -= hero_velocity / FPS
            else:
                pass

    def backward(self, axis_x, axis_y):
        # функция движения всей карты вниз
        t = True
        for object in self.objects:
            t = t and not (object.x - mouse_pos['x'] * mouse_impact + object.width >= hero_x and object.x - mouse_pos[
                'x'] * mouse_impact <= hero_x and object.y - mouse_pos[
                               'y'] * mouse_impact + object.height >= hero_y - 9 and object.y - mouse_pos[
                               'y'] * mouse_impact + object.height * 0.6 <= hero_y)
        for object in self.objects:
            if t:
                if axis_y == 1:
                    object.y += hero_velocity / FPS / (2 ** 0.5)
                else:
                    object.y += hero_velocity / FPS
            else:
                pass

    def left(self, axis_x, axis_y):
        # функция движения всей карты влево
        t = True
        for object in self.objects:
            t = t and not (object.x - mouse_pos['x'] * mouse_impact <= hero_x + 9 and object.x - mouse_pos[
                'x'] * mouse_impact + object.width * 0.4 >= hero_x and object.y - mouse_pos[
                               'y'] * mouse_impact <= hero_y and object.y - mouse_pos[
                               'y'] * mouse_impact + object.height >= hero_y)
        for object in self.objects:
            if t:
                if axis_x == 1:
                    object.x -= hero_velocity / FPS / (2 ** 0.5)
                else:
                    object.x -= hero_velocity / FPS
            else:
                pass

    def right(self, axis_x, axis_y):
        # функция движения всей карты вправо
        t = True
        for object in self.objects:
            t = t and not (object.x - mouse_pos['x'] * mouse_impact + object.width * 0.6 <= hero_x and object.x -
                           mouse_pos['x'] * mouse_impact + object.width >= hero_x - 9 and object.y - mouse_pos[
                               'y'] * mouse_impact <= hero_y and object.y - mouse_pos[
                               'y'] * mouse_impact + object.height >= hero_y)
        for object in self.objects:
            if t:
                if axis_x == 1:
                    object.x += hero_velocity / FPS / (2 ** 0.5)
                else:
                    object.x += hero_velocity / FPS
            else:
                pass


class Wall():
    def __init__(self, x, y, width, height):
        """ Конструктор класса wall
        Args:
        x - положение стены по горизонтали
        y - положение стены по вертикали
        width - длина
        height - высота
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = black

    def draw(self):
        # функция рисования стены на карте
        pygame.draw.rect(screen, black, (
            self.x - mouse_pos['x'] * mouse_impact, self.y - mouse_pos['y'] * mouse_impact, self.width, self.height))


class Hero:
    def __init__(self):
        """ Конструктор класса hero
        """
        self.color = black

    def draw(self):
        # функция рисования героя на карте
        pygame.draw.rect(screen, black, (hero_x - hero_size['x'] / 2, hero_y - hero_size['y'] / 2, 10, 10))


class Doors():
    """
    Конструктор дверей. Герой и боты не проходят сквозь них, однако у ботов есть возможность открыть двери моментально,
    если они находятся на определенном расстоянии от них. Герой должен взломать её.
    """

    def __init__(self, x, y, width, height, angle, interaction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.interaction = interaction

    def draw(self):
        if self.interaction:
            pygame.draw.line(screen, color_of_doors, (self.x - mouse_pos['x'] * mouse_impact, self.y + self.height/2 - mouse_pos['y'] * mouse_impact), (self.x - mouse_pos['x'] * mouse_impact + self.width * int(math.cos(self.angle)),
                                                                        self.y + self.height/2  - mouse_pos['y'] * mouse_impact - self.width * int(math.sin(self.angle))),
                             self.height)
        else:
            pygame.draw.line(screen, color_of_doors, (self.x - mouse_pos['x'] * mouse_impact, self.y - mouse_pos['y'] * mouse_impact),
                             (self.x - mouse_pos['x'] * mouse_impact + self.width * int(math.cos(self.angle + math.pi / 2)),
                              self.y - mouse_pos['y'] * mouse_impact - self.width * int(math.sin(self.angle + math.pi / 2))),
                             self.height)

    def door_interaction(self):
        pass


hero = Hero()
doors = [Doors(100, 100, 50, 16, 0, 1)]
walls = [Wall(200, 200, 600, 16), Wall(200, 200, 16, 200), Wall(200, 400, 200, 16), Wall(800, 200, 16, 200),
         Wall(440, 400, 376, 16)]
mymap = all_map(walls + doors)


pygame.display.update()
clock = pygame.time.Clock()

flag = {'forward': 0, 'backward': 0, 'left': 0, 'right': 0}
scripts = {'forward': mymap.forward, 'backward': mymap.backward, 'left': mymap.left, 'right': mymap.right}
buttons = {'forward': pygame.K_s, 'backward': pygame.K_w, 'left': pygame.K_d, 'right': pygame.K_a}
axis = {'Ox': 0, 'Oy': 0}

while 1:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            for key in buttons:
                if event.key == buttons[key]:
                    flag[key] = 1
                    if (flag['left'] == 1 or flag['right'] == 1) and flag['left'] != flag['right']:
                        axis['Oy'] = 1
                    if (flag['forward'] == 1 or flag['backward'] == 1) and flag['forward'] != flag['backward']:
                        axis['Ox'] = 1

        if event.type == pygame.MOUSEMOTION:
            mouse_pos['x'], mouse_pos['y'] = event.pos
            hero_x, hero_y = screen_width / 2 * (1 + mouse_impact) - mouse_pos[
                'x'] * mouse_impact, screen_height / 2 * (1 + mouse_impact) - hero_size['y'] / 2 - mouse_pos[
                                 'y'] * mouse_impact

        if event.type == pygame.KEYUP:
            for key in buttons:
                if event.key == buttons[key]:
                    flag[key] = 0
                    if (flag['left'] != 1 and flag['right'] != 1) or flag['left'] == flag['right']:
                        axis['Oy'] = 0
                    if (flag['forward'] != 1 and flag['backward'] != 1) or flag['forward'] == flag['backward']:
                        axis['Ox'] = 0

    for key in flag:
        if flag[key]:
            scripts[key](axis['Ox'], axis['Oy'])

    mymap.render()
    hero.draw()
    pygame.display.update()
