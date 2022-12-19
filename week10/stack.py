class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = [None] * max_size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, value):
        if self.top == self.max_size - 1:
            raise Exception("StackOverFlow")
        self.top += 1
        self.elements[self.top] = value

    def pop(self):
        if self.top == -1:
            raise Exception("StackUnderFlowError")
        value = self.elements[self.top]
        self.top -= 1
        return value