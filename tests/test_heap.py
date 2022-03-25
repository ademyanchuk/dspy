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
    h.insert(100)
    assert heap._is_max_heap(h)
