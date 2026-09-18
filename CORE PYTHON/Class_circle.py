import math

class Circle:

    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def circumference(self):
        return 2 * math.pi * self.radius

    @staticmethod
    def validate_radius(radius):
        return radius > 0

radius = 10
if Circle.validate_radius(radius):
    c1 = Circle(radius)
    print("Radius:", c1.radius)
    print("Area:", c1.area())
    print("Circumference:", c1.circumference())
else:
    print("Invalid radius")