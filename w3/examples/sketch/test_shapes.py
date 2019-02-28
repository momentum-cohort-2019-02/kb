from shapes import Circle, Rectangle, Square
import math


def test_circle_area():
    small_circle = Circle((0, 0), 1)
    assert small_circle.get_area() == math.pi

    larger_circle = Circle((0, 0), 2)
    assert larger_circle.get_area() == math.pi * 4


def test_rectangle_area():
    rectangle = Rectangle((0, 0), 5, 8)
    assert rectangle.get_area() == 40


def test_square_area():
    square = Square((0, 0), 6)
    assert square.get_area() == 36
