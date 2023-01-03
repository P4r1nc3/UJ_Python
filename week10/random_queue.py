import random

class RandomQueue:
    def __init__(self, size):
        self.elements = []
        self.size = size

    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full!")
        self.elements.append(item)

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        index = random.randint(0, len(self.elements) - 1)
        self.elements[index], self.elements[-1] = self.elements[-1], self.elements[index]
        return self.elements.pop()

    def is_empty(self):
        return len(self.elements) == 0

    def is_full(self):
        return len(self.elements) == self.size

    def clear(self):
        self.elements = []