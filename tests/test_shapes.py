import pytest
from shapes import Point, Line, Circle, Rectangle

def test_point_distance():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance(p2) == 5.0

def test_line_length():
    line = Line(Point(0, 0), Point(3, 4))
    assert line.length() == 5.0

def test_circle_area():
    circle = Circle(Point(0, 0), 5)
    assert circle.area() == pytest.approx(78.5398, 0.001)

def test_rectangle_perimeter():
    rect = Rectangle(Point(0, 0), Point(3, 4))
    assert rect.perimeter() == 14.0