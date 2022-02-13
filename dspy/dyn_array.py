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
        self._raise_if_out_range(idx)
        return self._arr[idx]

    def __setitem__(self, idx: int, val: Any):
        self._raise_if_out_range(idx)
        self._arr[idx] = val

    def __repr__(self) -> str:
        return f"{__class__.__name__}(val=None)"

    def __str__(self) -> str:
        return "DynamicArray([" + ",".join(str(n) for n in self) + "])"

    def append(self, val: Any):
        if len(self) == self._cap:
            self._resize(self._cap * 2)
        self._arr[len(self)] = val
        self._size += 1

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
        if idx >= self._size:
            raise IndexError("list index out of range")
