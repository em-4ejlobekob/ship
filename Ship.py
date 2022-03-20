from Game import Game
import pygame


class Ship(Game):

    def __init__(self, size, rotation, x, y, field):
        Game.__init__(self)
        self.size = size
        self.rotation = rotation
        if rotation == 'H':
            self.dx = 0
            self.dy = 1
        else:
            self.dx = 1
            self.dy = 0
        self.x = x
        self.y = y
        self.hits = 0
        self.cells = []
        for i in range(0, size):
            self.cells.append([self.x + self.dx * i, self.y + self.dy * i])

    def draw(self):
        a, b = self.x, self.y
        if self.rotation == 'H':
            for j in range(self.size):
                self.project_name.blit(pygame.image.load('BLUE.png'), (a, b))
                a += 38
        else:
            for j in range(self.size):
                self.project_name.blit(pygame.image.load('BLUE.png'), (a, b))
                b += 38
