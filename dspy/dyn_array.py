"""Implementation of Dynamic Array"""
import ctypes
from typing import Any, Optional, Sequence


class DynamicArray:
    """Own implementation of dynamicaly
    resizable array data structure. Implementation
    is using ctypes py_object to make a array similar
    to python built-in list.
    """

    def __init__(self, val: Optional[Sequence[Any]] = None) -> None:
        self._cap = 8  # capacity
        self._size = 0  # number of populated elements
        if val:
            self._cap = int(2 * len(val))

        self._arr = self._make_array(self._cap)
        if val:
            for i, v in enumerate(val):
                self._arr[i] = v
                self._size += 1

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, idx: int):
        idx = self._normalize_idx(idx)
        self._raise_if_out_range(idx)
        return self._arr[idx]

    def __setitem__(self, idx: int, val: Any):
        idx = self._normalize_idx(idx)
        self._raise_if_out_range(idx)
        self._arr[idx] = val

    def __repr__(self) -> str:
        return f"{__class__.__name__}(val=None)"

    def __str__(self) -> str:
        return "DynamicArray([" + ",".join(str(n) for n in self) + "])"

    def append(self, val: Any):
        """Push (pythonic append) ammortized O(1)

        Args:
            val (Any): value to append to the end of
            the array
        """
        self._maybe_grow()
        self._arr[len(self)] = val
        self._size += 1

    def insert(self, idx: int, val: Any):
        """Insert `val` at index `idx` and
        shift the rest of an array after `idx`
        one step to the right

        Args:
            idx (int): valid array index
            val (Any): value to insert
        """
        idx = self._normalize_idx(idx)
        self._raise_if_out_range(idx)
        self._maybe_grow()

        end = len(self) - 1
        for i in range(end, idx - 1, -1):
            self._arr[i + 1] = self[i]
        self._size += 1

        self[idx] = val

    def _make_array(self, capacity: int):
        return (capacity * ctypes.py_object)()

    def _resize(self, new_cap: int):
        """Resize dynamic array to have new capacity
        Note: it updates self._cap value, do not do
        it manually

        Args:
            new_cap (int): new capacity size
        """
        _arr = self._make_array(new_cap)
        self._cap = new_cap
        for i, v in enumerate(self):
            _arr[i] = v
        self._arr = _arr

    def _raise_if_out_range(self, idx: int):
        if idx >= self._size or idx < 0:
            raise IndexError("list index out of range")

    def _maybe_grow(self):
        """Helpper to increase capacity"""
        if len(self) == self._cap:
            self._resize(self._cap * 2)

    def _normalize_idx(self, idx: int) -> int:
        """Helper to convert index to its
        positive representation. If it is
        negative after conversio, it is out
        of list range (to the left so to say)

        Args:
            idx (int): index to convert

        Returns:
            [int]: index after conversion
        """
        if idx >= 0:
            return idx
        else:
            return len(self) + idx
