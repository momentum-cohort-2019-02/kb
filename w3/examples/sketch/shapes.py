import math
from PIL import Image, ImageDraw


class Shape:

    def __init__(self, origin):
        print("Shape.__init__")
        self.origin = origin

    def get_area(self):
        raise NotImplementedError


class Circle(Shape):

    def __init__(self, center, radius):
        print("Circle.__init__")
        super().__init__(center)
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)


class Rectangle(Shape):

    def __init__(self, topleft, width, length):
        print("Rectangle.__init__")
        super().__init__(topleft)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


class Square(Rectangle):

    def __init__(self, topleft, side):
        print("Square.__init__")
        super().__init__(topleft, side, side)


if __name__ == "__main__":
    img = Image.new('RGB', (100, 100), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    square = Square((50, 50), 30)
    draw.rectangle([
        square.origin,
        (square.origin[0] + square.width, square.origin[1] + square.length)
    ],
                   fill=0)
    img.save("test.jpg", "JPEG")
