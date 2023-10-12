from area.shape import Shape


class Parallelogram(Shape):
    def __init__(self, base, height):
        self.paral_area = 0.0
        self.base = base
        self.height = height

    def __str__(self) -> str:
        return ('Parallelogram Area of base ' + str(self.base) + 'U and height '
                + str(self.height) + 'U : ' + str(self.area()))

    def area(self):
        self.paral_area = self.base * self.height
        return self.paral_area
