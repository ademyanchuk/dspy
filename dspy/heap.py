"""Max Heap Implementation for integers"""


from typing import List


class Heap:
    def __init__(self) -> None:
        self._store = []

    def __len__(self) -> int:
        return len(self._store)

    def insert(self, val: int) -> None:
        """Insert value to max-heap.
        Sift it up if necessary

        Args:
            val (int): value to insert
        """
        self._store.append(val)
        idx = len(self) - 1
        self._sift_up(idx)

    def _sift_up(self, idx: int) -> None:
        # at root
        if idx == 0:
            return
        parent_idx = _parent_id(idx)
        if self._store[idx] > self._store[parent_idx]:
            self._store[parent_idx], self._store[idx] = (
                self._store[idx],
                self._store[parent_idx],
            )
            self._sift_up(parent_idx)

    def get_max(self) -> int:
        self._raise_empty()
        return self._store[0]

    def extract_max(self) -> int:
        self._raise_empty()
        # make root last element
        self._store[0], self._store[-1] = self._store[-1], self._store[0]
        # store value and delete last (former root)
        value = self._store.pop()
        # sift down if necessary
        self._sift_down(0)
        return value

    def _sift_down(self, idx: int) -> None:
        lch_id = _left_child_id(idx)
        rch_id = _right_child_id(idx)
        not_left = lch_id >= len(self)
        not_right = rch_id >= len(self)
        if not_left and not_right:
            return
        if not_left:
            max_id = rch_id
        elif not_right:
            max_id = lch_id
        else:
            max_id = lch_id if self._store[lch_id] > self._store[rch_id] else rch_id
        # swap if max child is > parent
        if self._store[idx] < self._store[max_id]:
            self._store[idx], self._store[max_id] = (
                self._store[max_id],
                self._store[idx],
            )
            # call recursively, if need to sift further down
            self._sift_down(max_id)

    def _heapify(self, values: List[int]):
        pass

    def _raise_empty(self):
        if not self:
            raise IndexError("Trying to access empty heap")


def heap_sort(arr: List[int]):
    pass


def _is_max_heap(heap: Heap, idx: int = 0) -> bool:
    """Helper to check max-heap invariant

    Args:
        heap (Heap): heap to check
        idx (int, optional): index to start. Defaults to 0.

    Returns:
        bool: True if invariant holds, False otherwise
    """
    if not heap._store:
        return True
    left_idx = _left_child_id(idx)
    right_idx = _right_child_id(idx)
    left = True
    if left_idx < len(heap):
        left = heap._store[idx] >= heap._store[left_idx]
        left = left and _is_max_heap(heap, left_idx)
    right = True
    if right_idx < len(heap):
        right = heap._store[idx] >= heap._store[right_idx]
        right = right and _is_max_heap(heap, right_idx)
    return left and right


def _left_child_id(idx: int) -> int:
    return 2 * idx + 1


def _right_child_id(idx: int) -> int:
    return 2 * idx + 2


def _parent_id(idx: int) -> int:
    return (idx - 1) // 2
