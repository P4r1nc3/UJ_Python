import math 
from points import Point
from cmath import pi

"""Klasa reprezentująca okręgi na płaszczyźnie."""
class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    # "Circle(x, y, radius)"
    def __repr__(self):
        return "Circle(%s, %s, %s)" % (self.pt.x, self.pt.y, self.radius)
    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    # pole powierzchni
    def area(self):
        return pi * self.radius**2
    
    # przesuniecie o (x, y)
    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)
    
    # najmniejszy okrąg pokrywający oba
    def cover(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Other must be Circle")
        dx = other.pt.x - self.pt.x
        dy = other.pt.y - self.pt.y
        dc = math.sqrt(dx**2 + dy**2)
        rmin = min(self.radius, other.radius)
        rmax = max(self.radius, other.radius)
        if rmin + dc < rmax:
            if self.radius > other.radius:
                x = self.pt.x
                y = self.pt.y
            else:
                x = other.pt.x
                y = other.pt.y
            R = rmax
        else:
            R = 0.5 * (self.radius + other.radius + dc)
            x = self.pt.x + (R - self.radius) * dx / dc
            y = self.pt.y + (R - self.radius) * dy / dc
        return Circle(x, y, R)
    
    @classmethod
    def from_points (cls, points):
        if not isinstance(points, (list, tuple)):
            raise TypeError("Points must either be a list or a tuple")

        A = points[0].x * (points[1].y - points[2].y) - points[0].y * (points[1].x - points[2].x) + points[1].x * points[2].y - points[2].x * points[1].y
        B = (points[0].x ** 2 + points[0].y ** 2) * (points[2].y - points[1].y) + (points[1].x ** 2 + points[1].y ** 2) * (points[0].y - points[2].y) + (points[2].x ** 2 + points[2].y ** 2) * (points[1].y - points[0].y)
        C = (points[0].x ** 2 + points[0].y ** 2) * (points[1].x - points[2].x) + (points[1].x ** 2 + points[1].y ** 2) * (points[2].x - points[0].x) + (points[2].x ** 2 + points[2].y ** 2) * (points[0].x - points[1].x)
        D = (points[0].x ** 2 + points[0].y ** 2) * (points[2].x * points[1].y - points[1].x * points[2].y) + (points[1].x ** 2 + points[1].y ** 2) * (points[0].x * points[2].y - points[2].x * points[0].y) + (points[2].x ** 2 + points[2].y ** 2) * (points[1].x * points[0].y - points[0].x * points[1].y)
       
        x = -B/(2*A)
        y = -C/(2*A)
        R = math.sqrt((B ** 2 + C ** 2 - 4*A*D)/(4*A ** 2))
        
        return cls(x, y, R)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return self.radius*2

    @property
    def height(self):
        return self.radius*2

    @property
    def topleft(self):
        return Point(self.pt.x - self.radius, self.pt.y + self.radius)

    @property
    def bottomleft(self):
        return Point(self.pt.x - self.radius, self.pt.y - self.radius)

    @property
    def topright(self):
        return Point(self.pt.x + self.radius, self.pt.y + self.radius)

    @property
    def bottomright(self):
        return Point(self.pt.x + self.radius, self.pt.y - self.radius)