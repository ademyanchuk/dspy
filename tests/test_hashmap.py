from dspy.hashmap import MyHashMap


def test_init():
    hm = MyHashMap()
    assert hm._size == 0
    assert all(el is None for el in hm._table)


def test_key2idx():
    hm = MyHashMap()
    assert all(
        [
            hm._key2idx(key, trial, hm._cap) in range(hm._cap)
            for key, trial in zip([321, 12, 100, 54234], [0, 1, 2, 3])
        ]
    )


def test_add_item():
    cap = 16
    table = [None] * cap
    items = [(0, 10), (1, 11), (0 + cap, 100), (1 + cap, 110)]
    hm = MyHashMap()
    for key, value in items:
        hm._add_item(key, value, table)
    assert all(item in table for item in items)
