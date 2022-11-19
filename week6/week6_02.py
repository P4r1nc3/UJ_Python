import math
import unittest

"""Klasa reprezentująca punkty na płaszczyźnie."""
class Point:
    # konstuktor
	def __init__(self, x=0, y=0):  
		self.x = x
		self.y = y

    # zwraca string "(x, y)"
	def __str__(self):
		return "(" + repr(self.x) + ", " + repr(self.y) + ")"

     # zwraca string "Point(x, y)"
	def __repr__(self):
		return self.__class__.__name__ + "(" + repr(self.x) + ", " + repr(self.y) + ")"

    # obsluga point1 == point2
	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

    # obsluga point1 != point2
	def __ne__(self, other):   
		if self.x != other.x or self.y != other.y:
			return True
		else:
			return False

    # v1 + v2
	def __add__(self, other):  
		return Point(self.x + other.x, self.y + other.y)

    # v1 - v2
	def __sub__(self, other): 
		return Point(self.x - other.x, self.y - other.y)

    # v1 * v2, iloczyn skalarny
	def __mul__(self, other): 
		return self.x * other.x + self.y * other.y

    # v1 x v2, iloczyn wektorowy 2D
	def cross(self, other):	
		return self.x * other.y - self.y * other.x

    # dlugosc wektora
	def length(self): 
		return math.sqrt(self.x ** 2.0 + self.y ** 2.0)

# Przykładowe dwa punkty
p1 = Point(1,2)
p2 = Point(3,4)

class TestPoint(unittest.TestCase):
	def test__str__(self):
		self.assertEqual(p1.__str__(), "(1, 2)")

	def test__repr__(self):
		self.assertEqual(p1.__repr__(), "Point(1, 2)")

	def test__eq__(self):
		self.assertFalse(p1.__eq__(p2))

	def test__ne__(self):
		self.assertTrue(p1.__ne__(p2))

	def test__add__(self):
		self.assertEqual(p1.__add__(p2),Point(4, 6))

	def test__sub__(self):
		self.assertEqual(p1.__sub__(p2),Point(-2, -2))

	def test__mul__(self):
		self.assertEqual(p1.__mul__(p2), 11)

	def testcross(self):
		self.assertEqual(p1.cross(p2), -2)

	def testlength(self):
		self.assertEqual(p1.length(), math.sqrt(5))

if __name__ == '__main__':
	unittest.main()     