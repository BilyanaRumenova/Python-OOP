from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    WEIGHT_OF_ANIMAL = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        return super().feed(food)


class Hen(Bird):
    WEIGHT_OF_ANIMAL = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        return super().feed(food)
