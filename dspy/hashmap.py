"""Hash Map Implementation. Interface corresponds to leetcode problem 706. Design HashMap
Simplified int->int variant (key is a positive integer)

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

- MyHashMap() initializes the object with an empty map.

- void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.

- int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.

- void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""


from collections import namedtuple
from typing import Any, List, Optional

DEL_FLAG = "_DEL_"

Item = namedtuple("Item", ["key", "value"])


class MyHashMap:
    """Open Addressing Implementation"""

    def __init__(self):
        self._cap = 32
        self._size = 0
        self._table = [None] * self._cap
        self._hashfn = hash

    def _hash(self, key: int, trial: int) -> int:
        """Hash function for open addressing
        hashmap implementation

        Args:
            key (int): key
            trial (int): attempt to find open address

        Returns:
            int: hash from key + trial
        """
        return hash(key + trial)

    def _key2idx(self, key: int, trial: int, m: int) -> int:
        """Convert key to internal table index

        Args:
            key (int): key
            m (int): table size

        Returns:
            int: table index
        """
        return self._hash(key, trial) % m

    def _add_item(self, key: int, value: int, table: List[Optional[Item]]) -> None:
        trial = 0
        cap = len(table)
        item = Item(key, value)
        idx = self._key2idx(key, trial, cap)
        while table[idx] not in [None, DEL_FLAG]:
            # update
            if table[idx].key == item.key:
                table[idx] = item
            trial += 1
            idx = self._key2idx(key, trial, cap)
        # open address, can add item
        table[idx] = item

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def remove(self, key: int) -> None:
        raise NotImplementedError


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
