import my_array


class MyQueue(my_array.MyArray):
    def __init__(self, capacity: int) -> None:
        super().__init__(capacity)

    def dequeue(self) -> int:
        if self.is_empty():
            return None

        return self._data.pop(0)

    def enqueue(self, value: int) -> None:
        return super().push(value)

    def front(self) -> int:
        if self.is_empty():
            return None

        return self._data[0]


# Test MyQueue
queue1 = MyQueue(capacity=5)
queue1.push(1)
queue1.push(2)

assert queue1.is_full() == False
assert queue1.front() == 1
assert queue1.dequeue() == 1
assert queue1.front() == 2
assert queue1.dequeue() == 2
assert queue1.is_empty() == True
