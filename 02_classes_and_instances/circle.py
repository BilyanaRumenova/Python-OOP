class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius

    def get_area(self):
        area = Circle.pi * self.radius * self.radius
        return area

    def get_circumference(self):
        return 2 * Circle.pi * self.radius
