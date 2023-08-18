from circles import Circle
from points import Point

def test_from_points():
    circle = Circle.from_points([Point(-6, 3), Point(-3, 2), Point(0, 3)])
    assert str(circle) == 'Circle(-3.0, 7.0, 5.0)'

def test_properties():
    circle = Circle(0, 0, 5)

    assert circle.top == 5
    assert circle.bottom == -5

    assert circle.left == -5
    assert circle.right == 5

    assert circle.height == 10
    assert circle.width == 10

    assert circle.topleft == Point(-5, 5)
    assert circle.bottomleft == Point(-5, -5)

    assert circle.topright == Point(5, 5)
    assert circle.bottomright == Point(5, -5)

test_properties()
test_from_points()