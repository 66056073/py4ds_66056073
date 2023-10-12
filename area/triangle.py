from area.shape import Shape


class Triangle(Shape):
    def __init__(self, base, height):
        self.tri_area = 0.0
        self.base = base
        self.height = height

    def __str__(self) -> str:
        return ('Triangle Area of base ' + str(self.base) + 'U and height '
                + str(self.height) + 'U : ' + str(self.area()))

    def area(self):
        self.tri_area = 0.5 * self.base * self.height
        return self.tri_area
