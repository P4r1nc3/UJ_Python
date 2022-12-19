from random_queue import RandomQueue
import unittest

class TestRandomQueue(unittest.TestCase):
    def test_insert_and_remove(self):
        queue = RandomQueue(5)

        queue.insert(1)
        self.assertEqual(queue.remove(), 1)

    def test_is_empty_and_is_full(self):
        queue = RandomQueue(2)

        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())

        queue.insert(1)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())

        queue.insert(2)
        self.assertFalse(queue.is_empty())
        self.assertTrue(queue.is_full())

    def test_clear(self):
        queue = RandomQueue(5)

        queue.insert(1)
        queue.insert(2)
        queue.insert(3)

        queue.clear()
        self.assertTrue(queue.is_empty())

    def test_queue_full(self):
        queue = RandomQueue(2)

        queue.insert(1)
        queue.insert(2)

        with self.assertRaises(Exception) as context:
            queue.insert(3)
        self.assertEqual(str(context.exception), "Queue is full!")

    def test_queue_empty(self):
        queue = RandomQueue(2)

        with self.assertRaises(Exception) as context:
            queue.remove()
        self.assertEqual(str(context.exception), "Queue is empty!")

if __name__ == '__main__':
    unittest.main()