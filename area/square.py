from area.shape import Shape


class Square(Shape):
    def __init__(self, width):
        self.sqr_area = 0.0
        self.width = width

    def area(self):
        self.sqr_area = self.width * self.width
        return self.sqr_area

    def __str__(self) -> str:
        return 'Square Area of ' + str(self.width) + 'U :' + str(self.area())
