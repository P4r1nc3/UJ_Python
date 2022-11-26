import math 
import unittest
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

c1 = Circle(0, 0, 4)
c2 = Circle(-2, -2, 4)
print(c1.cover(c2))

class TestCircle(unittest.TestCase):	    
    def testRepr(self):
        self.assertEqual(c1.__repr__() , "Circle(0, 0, 4)")
        self.assertEqual(c2.__repr__() , "Circle(-2, -2, 4)")	

    def testEq(self):
        self.assertTrue(c1.__eq__(c1))
        self.assertFalse(c2.__eq__(c1))

    def testNe(self):
        self.assertTrue(c1.__ne__(c2))
        self.assertTrue(c2.__ne__(c1))

    def testArea(self):
        self.assertEqual(c1.area(), 50.26548245743669)
        self.assertEqual(c2.area(), 50.26548245743669)

    def testMove(self):
        self.assertEqual(c1.move(0,2), Circle(0,2,4))
        self.assertEqual(c2.move(0,2), Circle(-2,0,4))

    def testCover(self):
        self.assertEqual(c1.cover(c2), Circle(-0.9999999999999999, -0.9999999999999999, 5.414213562373095))

if __name__ == '__main__':
	unittest.main()