"""Singly LinkedList and common functionality Implemantation"""
import re
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class ListNode(Generic[T]):
    """Single Element of a LinkedList, which
    holds a data and a poiner to the next node"""

    def __init__(self, value: T, next: Optional["ListNode[T]"] = None) -> None:
        self.data = value
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(value={self.data!r}, next={self.next!r})"

    def __str__(self) -> str:
        return f"{self.data!s}"


class LinkedList(Generic[T]):
    """Singly LinkedList"""

    def __init__(self, value: Optional[T] = None) -> None:
        """Initialize empty instance or provide a value
        and initialize with one node"""
        self.head = None
        self.tail = None
        self._size = 0
        if value is not None:
            self.head = ListNode(value)
            self.tail = self.head
            self._size += 1

    def __len__(self):
        return self._size

    def __getitem__(self, idx: int):
        """get item is O(n) time complexity"""
        if len(self) <= idx:
            raise IndexError("linked list index out of range")
        cur = self.head
        i = 0
        while i < idx:
            cur = cur.next  # noqa we've checked idx is valid
            i += 1
        return cur

    def __repr__(self) -> str:
        return f"{__class__.__name__}(value={self.head!s})"

    def __str__(self) -> str:
        return "LinkedList([" + ",".join(str(n) for n in self) + "])"

    def push_front(self, value: T):
        """Push a node with `value` in front of
        the linked list

        Args:
            value (T): data value
        """
        node = ListNode(value, self.head)
        self.head = node
        if not self:  # empty list
            self.tail = self.head
        self._size += 1

    def pop_front(self) -> T:
        """Pop a node from the front of the
        linked list and returns its data value

        Raises:
            IndexError: if trying to pop from empty list

        Returns:
            T: data value of the head node
        """
        if not self:
            raise IndexError("pop from empty linked list")
        tmp = self.head
        value = tmp.data
        self.head = tmp.next
        del tmp

        self._size -= 1
        if not self:
            # drop tail as well
            self.tail = self.head
        return value

    def push_back(self, value: T):
        """Push a node with data `value` to the
        back of linked list

        Args:
            value (T): value of the element to push
        """
        node = ListNode(value)
        if not self:
            # list is empty, just assign head and tail to the node
            self.tail = node
            self.head = self.tail
        else:
            tmp = self.tail
            self.tail = node
            tmp.next = self.tail
        self._size += 1

    def pop_back(self) -> T:
        """Will pop the node from back and return its value

        Raises:
            IndexError: if trying to pop from empty list

        Returns:
            T: value of the node at the back of the
            linked list
        """
        if not self:
            raise IndexError("pop from empty linked list")
        value = self.tail.data
        if len(self) == 1:
            self.tail = None
            self.head = self.tail
        else:
            self.tail = self[-2]  # it is O(n) operation
        self._size -= 1
        return value

    def peek_front(self) -> T:
        """Helper to just peek a front value. User can
        access linked list elements through indexing syntax

        Raises:
            IndexError: if peeking into empty list

        Returns:
            T: data value of front node
        """
        if not self:
            raise IndexError("peek from empty linked list")
        return self.head.data

    def peek_back(self) -> T:
        """Helper to just peek a back value. User can
        access linked list elements through indexing syntax

        Raises:
            IndexError: if peeking into empty list

        Returns:
            T: data value of front node
        """
        if not self:
            raise IndexError("peek from empty linked list")
        return self.tail.data
