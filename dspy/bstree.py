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
    def __init__(self, values: Optional[List[Any]] = None) -> None:
        self.root = None
        self.__dtype = None
        if values:
            self._from_values(values)

    def __contains__(self, val: Any) -> bool:
        return not self.find(val) is None

    # NOTE! Remember, if recursive function called with None object
    # it brakes referencing to the not-None object and you modify nothing
    # if _insert takes node=None, and then try to assign some value to it,
    # this evaluates into None = TreeNode(val) and breaks the recursive chain!
    def insert(self, val: Any) -> bool:
        """Insert a Node with value `val` in the tree
        according to BS Tree invariant. Value type mis-
        match and duplicates are not allowed

        Args:
            val (Any): value to insert

        Returns:
            bool: True if successfully insert a value,
            False otherwise [incorrect value type,
            duplicate]
        """
        self._dtype = val
        try:
            self._check_dtype_mismatch(val)
        except AttributeError:
            return False

        # duplicates are not allowed
        if val in self:
            return False

        def _insert(node: Optional[TreeNode], val: Any) -> TreeNode:
            if node is None:
                return TreeNode(val=val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node

        self.root = _insert(self.root, val)
        return True

    def del_value(self, val: Any) -> bool:
        try:
            self._check_dtype_mismatch(val)
        except AttributeError:
            return False

        if self.find(val) is None:
            return False

        def _delete(node: Optional[TreeNode], val: Any) -> Optional[TreeNode]:
            if node is None:
                return node
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:  # delete this node
                # Cases one or both children is None
                # case left is None
                if node.left is None:
                    tmp = node.right
                    node = None
                    return tmp
                elif node.right is None:
                    tmp = node.left
                    node = None
                    return tmp
                # Two children case
                else:
                    # Find successor
                    suc = _first(node.right)
                    # Swap values
                    node.val, suc.val = suc.val, node.val
                    # Delete swapped node down in the right subtree
                    node.right = _delete(node.right, val)
            return node

        self.root = _delete(self.root, val)
        return True

    def _from_values(self, values: List[Any]):
        for val in values:
            self.insert(val)

    def inorder(self) -> List[Any]:
        """In order BS Tree traversal

        Returns:
            List[Any]: list of values [in order]
        """
        values = []

        def inner(node: Optional[TreeNode]):
            if not node:
                return
            inner(node.left)
            values.append(node.val)
            inner(node.right)

        inner(self.root)
        return values

    def find(self, val: Any) -> Optional[TreeNode]:
        """Find a Node containing a value `val`

        Args:
            val (Any): value to find

        Returns:
            Optional[TreeNode]: Node if `val` found,
            None otherwise
        """
        if not self.root:
            return None
        try:
            self._check_dtype_mismatch(val)
        except AttributeError:
            print(
                f"Trying to find incompatible value of type {type(val)}, in the Tree with type: {self._dtype}"
            )
            return None

        def _find(node: Optional[TreeNode], val: Any):
            if not node:
                return None
            if node.val == val:
                return node
            elif val < node.val:
                return _find(node.left, val)
            else:
                return _find(node.right, val)

        return _find(self.root, val)

    def height(self) -> int:
        """Returns tree height

        Returns:
            int: height represents a longest
            downward pass from the root (number
            of edges in the longest subtree from root)
        """

        def _height(node: Optional[TreeNode]) -> int:
            if node is None or _is_leaf(node):
                return 0
            return max(_height(node.left), _height(node.right)) + 1

        return _height(self.root)

    def min(self) -> Optional[Any]:
        if self.root is None:
            return None
        first = _first(self.root)
        return first.val

    def max(self) -> Optional[Any]:
        if self.root is None:
            return None
        last = _last(self.root)
        return last.val

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


def _is_leaf(node: TreeNode) -> bool:
    return not (node.left or node.right)


def _first(root: TreeNode) -> TreeNode:
    """Return a first in "inorder" traversal order
    of the `root` subtree

    Args:
        root (TreeNode): root of subtree

    Returns:
        TreeNode: first node in subtree
    """
    if root.left is None:
        return root
    return _first(root.left)


def _last(root: TreeNode) -> TreeNode:
    """Return a last in "inorder" traversal order
    of the `root` subtree

    Args:
        root (TreeNode): root of subtree

    Returns:
        TreeNode: last node in subtree
    """
    if root.right is None:
        return root
    return _last(root.right)
