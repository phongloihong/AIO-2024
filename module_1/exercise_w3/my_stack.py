import my_array


class MyStack(my_array.MyArray):
    def __init__(self, capacity: int) -> None:
        super().__init__(capacity)

    def pop(self) -> int:
        if self.is_empty():
            return None

        return self._data.pop()

    def top(self) -> int:
        if self.is_empty():
            return None

        return self._data[-1]


# Test MyStack
stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)

assert stack1.is_full() == False
assert stack1.top() == 2
assert stack1.pop() == 2
assert stack1.top() == 1
assert stack1.pop() == 1
assert stack1.is_empty() == True
