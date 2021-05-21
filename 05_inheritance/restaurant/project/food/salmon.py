# from inheritance_exercises.restaurant.project.food.main_dish import MainDish
from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.GRAMS)