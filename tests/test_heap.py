import random

import pytest

from dspy import heap


def test_heap_len():
    h = heap.Heap()
    h._store = [10, 3, 20]
    assert len(h) == 3


def test_is_max_heap_empty():
    h = heap.Heap()
    assert heap._is_max_heap(h)


def test_is_max_heap_one():
    h = heap.Heap()
    h._store = [10]
    assert heap._is_max_heap(h)


def test_is_max_heap_true():
    h = heap.Heap()
    h._store = [10, 8, 10, 7, 4, 8, 5, 3]
    assert heap._is_max_heap(h)


def test_is_max_heap_false():
    h = heap.Heap()
    h._store = [10, 3, 20]
    assert not heap._is_max_heap(h)


def test_is_max_heap_false_deep():
    h = heap.Heap()
    h._store = [10, 8, 10, 7, 4, 9, 2, 100]
    assert not heap._is_max_heap(h)


def test_insert_is_in():
    h = heap.Heap()
    h.insert(23)
    assert 23 in h._store


def test_insert_is_heap():
    h = heap.Heap()
    h.insert(23)
    h.insert(50)
    h.insert(100)
    h.insert(250)
    h.insert(120)
    assert heap._is_max_heap(h)
    print(h._store)


def test_get_max_raises():
    h = heap.Heap()
    with pytest.raises(IndexError, match="empty heap"):
        h.get_max()


def test_get_max():
    h = heap.Heap()
    h.insert(100)
    h.insert(509)
    h.insert(2)
    assert h.get_max() == max(h._store)


def test_extract_max():
    h = heap.Heap()
    h.insert(100)
    h.insert(509)
    h.insert(2)
    want = max(h._store)
    assert h.extract_max() == want
    assert want not in h._store


def test_extract_max_is_heap():
    h = heap.Heap()
    h.insert(500)
    h.insert(100)
    h.insert(2)
    h.extract_max()
    h.insert(300)
    h.insert(34)
    h.extract_max()
    assert heap._is_max_heap(h)


def test_heapify():
    values = [random.randint(-100, 300) for _ in range(100)]
    h = heap.Heap(values=values)
    print(h._store)
    assert heap._is_max_heap(h)
