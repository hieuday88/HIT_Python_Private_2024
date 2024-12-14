class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.size = 0

    def initialization(self, capacity):
        self.__capacity = capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def push(self, value):
        if self.isFull():
            return
        self.stack.append(value)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return
        self.size -= 1
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return
        return self.stack[-1]



stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())