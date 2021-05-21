from abc import ABC, abstractmethod


class Animal(ABC):
    WEIGHT_OF_ANIMAL = None

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @staticmethod
    def check_food():
        mapper = {
            "Vegetable": ["Cat", "Mouse", "Hen"],
            "Fruit": ["Mouse", "Hen"],
            "Meat": ["Cat", "Tiger", "Dog", "Owl", "Hen"],
            "Seed": ["Hen"]
        }
        return mapper

    def gain_weight(self, food):
        self.weight += self.WEIGHT_OF_ANIMAL * food.quantity

    def feed(self, food):
        if type(self).__name__ not in self.check_food()[food.__class__.__name__]:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.gain_weight(food)
        self.food_eaten += food.quantity


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"





