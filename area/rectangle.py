from area.shape import Shape


class Rect(Shape):

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.rect_area = 0.0

    def __str__(self) -> str:
        return ('Rectangle Area of '
                + str(self.width) + 'Ux' + str(self.height)
                + 'U :' + str(self.area()))

    def area(self):
        self.rect_area = self.width * self.height
        return self.rect_area
