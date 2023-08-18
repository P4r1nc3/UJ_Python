import unittest
from week6_02 import Point

"""Klasa reprezentująca prostokąt na płaszczyźnie."""
class Rectangle:
    # Konstruktor
    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):          
        return f'[{self.pt1}, {self.pt2}]'

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):        
       return "Rectangle(" + repr(self.pt1.x) + ", " + repr(self.pt1.y) + ", " + repr(self.pt2.x) + ", "+repr(self.pt2.y) + ")"

    # obsługa rect1 == rect2
    def __eq__(self, other):  
        return isinstance(other, Rectangle) and self.pt1 == other.pt1 and self.pt2 == other.pt2

    # obsługa rect1 != rect2
    def __ne__(self, other):        
        return not self == other

    # zwraca środek prostokąta
    def center(self):          
        return Point((self.pt1.x +self.pt2.x)/2 , (self.pt1.y + self.pt2.y)/2)

    # pole powierzchni
    def area(self):            
        return abs(self.pt1.x-self.pt2.x) * abs(self.pt1.y-self.pt2.y)

    # przesunięcie o (x, y)
    def move(self, x, y):
        return Rectangle(self.pt1.x+x , self.pt1.y+y , self.pt2.x+x , self.pt2.y+y)

# Przykładowe dwa prostokaty
r1 = Rectangle(0, 0, 4, 4)
r2 = Rectangle(-4, -4, -8, -8)

# Kod testujacy modul.
class TestRectangle(unittest.TestCase):
    def test__str__(self):
        self.assertEqual(r1.__str__(), "[(0, 0), (4, 4)]")
        self.assertEqual(r2.__str__(), "[(-4, -4), (-8, -8)]")

    def test__repr__(self):
        self.assertEqual(r1.__repr__(), "Rectangle(0, 0, 4, 4)")
        self.assertEqual(r2.__repr__(), "Rectangle(-4, -4, -8, -8)")

    def test__eq__(self):
        self.assertTrue(r1 == Rectangle(0, 0, 4, 4))
        self.assertFalse(r2 == Rectangle(0, 0, 4, 4))

    def test__ne__(self):
        self.assertFalse(r1 != Rectangle(0, 0, 4, 4))
        self.assertTrue(r1 != r2)

    def testcenter(self):
        self.assertEqual(r1.center(), Point(2, 2))
        self.assertEqual(r2.center(), Point(-6, -6))

    def testarea(self):
        self.assertEqual(r1.area(), 16)
        self.assertEqual(r1.area(), 16)

    def testmove(self):
        self.assertEqual(r1.move(1, 1), Rectangle(1, 1, 5, 5))
        self.assertEqual(r2.move(23, -21), Rectangle(19, -25, 15, -29))
        
if __name__ == '__main__':
    unittest.main()