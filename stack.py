class Stack:

    def __init__(self):
        self.stack = []


    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
