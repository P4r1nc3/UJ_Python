import unittest
import polys

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [2, 1]                   # W(x) = 2 + x
        self.p2 = [2, 1, 0]                # jw  (niejednoznaczność)
        self.p3 = [-3, 0, 1]               # W(x) = -3 + x^2
        self.p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
        self.p5 = [0]                      # zero
        self.p6 = [0, 0, 0]                # zero (niejednoznaczność)

    def test_add_poly(self):
        self.assertEqual(polys.add_poly(self.p1, self.p2), [4, 2])
        self.assertEqual(polys.add_poly(self.p3, self.p4), [0, 0, 1])

    def test_sub_poly(self):
        self.assertEqual(polys.sub_poly(self.p1, self.p2), [0])
        self.assertEqual(polys.sub_poly(self.p5, self.p3), [3, 0, -1])

    def test_mul_poly(self):
        self.assertEqual(polys.mul_poly(self.p2, self.p6), [0])
        self.assertEqual(polys.mul_poly(self.p3, self.p4), [-9, 0, 3])

    def test_is_zero(self):
        self.assertFalse(polys.is_zero(self.p3))
        self.assertTrue(polys.is_zero(self.p6))

    def test_eq_poly(self):
        self.assertFalse(polys.eq_poly(self.p3, self.p2))
        self.assertTrue(polys.eq_poly(self.p5, self.p6))
        
    def test_eval_poly(self):
        self.assertEqual(polys.eval_poly(self.p2, 5), 7)
        self.assertEqual(polys.eval_poly(self.p4, 2), 3)

    def test_combine_poly(self):
        self.assertEqual(polys.combine_poly(self.p1, self.p2), [4, 1])
        self.assertEqual(polys.combine_poly(self.p5, self.p4), [0])

    def test_pow_poly(self):
        self.assertEqual(polys.pow_poly(self.p1, 5), [32, 80, 80, 40, 10, 1])
        self.assertEqual(polys.pow_poly(self.p3, 3), [-27, 0, 27, 0, -9, 0, 1])

    def test_diff_poly(self): 
        self.assertEqual(polys.diff_poly(self.p1), [1])
        self.assertEqual(polys.diff_poly(self.p2), [1, 0])

if __name__ == '__main__':
    unittest.main()