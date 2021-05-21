import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        a = self.x - x
        b = self.y - y
        c = math.sqrt(a**2 + b**2)
        return c
