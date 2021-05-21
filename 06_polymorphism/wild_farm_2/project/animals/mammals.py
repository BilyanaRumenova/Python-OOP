from project.animals.animal import Mammal
from project.animals.birds import Owl, Hen
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_OF_ANIMAL = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        return super().feed(food)


class Dog(Mammal):
    WEIGHT_OF_ANIMAL = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        return super().feed(food)


class Cat(Mammal):
    WEIGHT_OF_ANIMAL = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        return super().feed(food)


class Tiger(Mammal):
    WEIGHT_OF_ANIMAL = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        return super().feed(food)


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)