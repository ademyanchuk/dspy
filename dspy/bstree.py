"""Binary Search Tree Implementation"""

import queue
from typing import Any, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTree:
    def __init__(self) -> None:
        self.root = None
        self.__dtype = None

    # NOTE! Remember, if recursive function called with None object
    # it brakes referencing to the not-None object and you modify nothing
    # if _insert takes node=None, and then try to assign some value to it,
    # this evaluates into None = TreeNode(val) and breaks the recursive chain!
    def insert(self, val: Any):
        self._dtype = val

        def _insert(node: TreeNode, val: Any):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    _insert(node.left, val)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    _insert(node.right, val)

        if self.root is None:
            self.root = TreeNode(val)
        else:
            _insert(self.root, val)

    @property
    def _dtype(self):
        return self.__dtype

    @_dtype.setter
    def _dtype(self, val):
        # if trying to reassign, pass
        if self.__dtype is not None:
            return
        # check if value is of comparable dtype
        self._check_dtype(val)
        self.__dtype = type(val)

    def _check_dtype(self, val: Any):
        # raise if value is not comparable
        if not hasattr(val, "__lt__"):
            raise AttributeError(f"{val} is not comparable")
        elif val.__lt__(val) == NotImplemented:
            raise AttributeError(f"{val} is not comparable")

    def _check_dtype_mismatch(self, val: Any):
        # allow only values of same type in the tree
        if self._dtype is not None:
            if not isinstance(val, self._dtype):
                raise AttributeError(f"Type mismatch: {type(val)} != {self._dtype}")


def level_traverse(root: Optional[TreeNode]) -> List[Any]:
    values = []
    fifo = queue.Queue()
    if root:
        fifo.put(root)
    while not fifo.empty():
        node = fifo.get()
        values.append(node.val)
        if lft := node.left:
            fifo.put(lft)
        if rht := node.right:
            fifo.put(rht)
    return values


# assume it is not binary search tree
def find_by_value(root: TreeNode, val: int) -> Optional[TreeNode]:
    if val == root.val:
        return root
    elif root.left is not None:
        return find_by_value(root.left, val)
    elif root.right is not None:
        return find_by_value(root.right, val)
    else:
        return None
