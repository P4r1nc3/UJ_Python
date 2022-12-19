import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def test_push_and_pop(self):
        stack = Stack(3)

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_is_empty_and_is_full(self):
        stack = Stack(2)

        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())

        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())

        stack.push(2)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())

    def test_stackoverflow(self):
        stack = Stack(2)

        stack.push(1)
        stack.push(2)

        with self.assertRaises(Exception) as context:
            stack.push(3)
        self.assertEqual(str(context.exception), "StackOverFlow")

    def test_stackunderflow(self):
        stack = Stack(2)

        with self.assertRaises(Exception) as context:
            stack.pop()
        self.assertEqual(str(context.exception), "StackUnderFlowError")

if __name__ == '__main__':
    unittest.main()