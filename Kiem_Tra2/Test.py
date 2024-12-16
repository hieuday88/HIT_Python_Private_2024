class Stack:
    def __init__(self, capacity: int):
        """
        Khoi tao stack

        Args:
            capacity (int): So phan tu toi da
        """
        self.capacity = capacity
        self.stack = []
        self.size = 0

    def is_empty(self) -> bool:
        """
        Kiem tra stack rong

        Returns:
            bool
        """
        return self.size == 0

    def is_full(self) -> bool:
        """
        Kiem tra stack day

        Returns:
            bool
        """
        return self.size == self.capacity

    def push(self, value: int) -> None:
        """
        Them phan tu vao cuoi

        Args:
            value (int): Gia tri them
        """
        if self.is_full():
            return
        self.stack.append(value)
        self.size += 1

    def pop(self) -> int | None:
        """
        Lay phan tu cuoi va xoa

        Returns:
            int | None: Gia tri phan tu hoac None neu stack rong
        """
        if self.is_empty():
            return None
        self.size -= 1
        return self.stack.pop()

    def top(self) -> int | None:
        """
        Lay phan tu cuoi

        Returns:
            int | None: Gia tri phan tu hoac None neu stack rong
        """
        if self.is_empty():
            return None
        return self.stack[-1]


stack1 = Stack(5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())  # False
print(stack1.top())  # 2
print(stack1.pop())  # 2
print(stack1.top())  # 1
print(stack1.pop())  # 1
print(stack1.is_empty())  # True