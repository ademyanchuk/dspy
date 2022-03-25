"""Max Heap Implementation for integers"""


from typing import List


class Heap:
    def __init__(self) -> None:
        self._store = []
        self._size = len(self._store)

    def __len__(self) -> int:
        return self._size

    def insert(self, val: int) -> None:
        pass

    def _sift_up(self, idx: int) -> None:
        pass

    def get_max(self) -> int:
        pass

    def extract_max(self) -> int:
        pass

    def _sift_down(self, idx: int) -> None:
        pass

    def _heapify(self, values: List[int]):
        pass


def heap_sort(arr: List[int]):
    pass
