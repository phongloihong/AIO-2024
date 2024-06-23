class MyArray:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._data = []

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def is_full(self) -> bool:
        return len(self._data) == self._capacity

    def push(self, value: int) -> None:
        if self.is_full():
            return None

        self._data.append(value)
