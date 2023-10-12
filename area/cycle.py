import math
from area.shape import Shape


class Cycle(Shape):
    def __init__(self, radius) -> None:
        self.cycle_area = 0.0
        self.radius = radius

    def __str__(self) -> str:
        return 'Cycle Area of radius ' + str(self.radius) + 'U : ' + str(self.area())

    def area(self):
        self.cycle_area = math.pi * pow(self.radius, 2)
        return self.cycle_area
