import math
from area.shape import Shape


class Oval(Shape):
    def __init__(self, a, b) -> None:
        self.oval_area = 0.0
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return 'Oval Area of a ' + str(self.a) + 'U and b ' + str(self.b) + 'U : ' + str(self.area())

    def area(self):
        self.oval_area = math.pi * self.a * self.b
        return self.oval_area
