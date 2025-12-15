class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        return self._data[-1] if self._data else None

    def is_empty(self):
        return len(self._data) == 0

# Example:
s = Stack()
s.push(10); s.push(20)
print(s.pop());print(s.peek())   # 20
# 10
