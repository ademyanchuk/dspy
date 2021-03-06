import random

import pytest

from dspy import sort


@pytest.fixture(scope="module")
def big():
    return random.sample(range(1_000_000), k=100_000)


def test_merge_empty():
    assert not sort.merge([], [])


def test_merge_one():
    a = [1, 2, 3]
    assert sort.merge(a, []) == a


def test_merge():
    a = [3, 5, 10, 21]
    b = [1, 7, 8]
    assert sort.merge(a, b) == sorted(a + b)


def test_merge_sort_empty():
    assert not sort.merge_sort([])


def test_merge_sort_one():
    assert sort.merge_sort([1]) == [1]


def test_merge_sort_even():
    a = [1, 10, 9, 2, 3, 18, 0, -1, 23, 2]
    assert sort.merge_sort(a) == sorted(a)


def test_merge_sort_odd():
    a = [1, 10, 9, 2, 3, 18, 0, -1, 23, 2, 12]
    assert sort.merge_sort(a) == sorted(a)


def test_merge_sort_big(big):
    assert sort.merge_sort(big) == sorted(big)


def test_quick_sort_empty():
    a = []
    sort.quick_sort(a, 0, len(a) - 1)
    assert not a


def test_quick_sort_one():
    a = [1]
    sort.quick_sort(a, 0, len(a) - 1)
    assert a == [1]


def test_quick_sort_even():
    a = [1, 10, 9, 2, 3, 18, 0, -1, 23, 2]
    want = sorted(a)
    sort.quick_sort(a, 0, len(a) - 1)
    assert a == want


def test_quick_sort_odd():
    a = [1, 10, 9, 2, 3, 18, 0, -1, 23, 2, 12]
    want = sorted(a)
    sort.quick_sort(a, 0, len(a) - 1)
    assert a == want


def test_quick_sort_big(big):
    want = sorted(big)
    sort.quick_sort(big, 0, len(big) - 1)
    assert big == want


def test_insertion_sort_empty():
    a = []
    sort.insertion_sort(a)
    assert not a


def test_insertion_sort_one():
    a = [1]
    sort.insertion_sort(a)
    assert a == [1]


def test_insertion_sort_even():
    a = [1, 10, 9, 2, 3, 18, 0, -1, 23, 2]
    want = sorted(a)
    sort.insertion_sort(a)
    assert a == want


def test_insertion_sort_odd():
    a = [1, 10, 9, 2, 3, 18, 0, -1, 23, 2, 12]
    want = sorted(a)
    sort.insertion_sort(a)
    assert a == want


def test_insertion_sort_big(big):
    big = big[:1000]
    want = sorted(big)
    sort.insertion_sort(big)
    assert big == want


def test_bubble_sort_empty():
    a = []
    sort.bubble_sort(a)
    assert not a


def test_bubble_sort_one():
    a = [1]
    sort.bubble_sort(a)
    assert a == [1]


def test_bubble_sort_even():
    a = [1, 10, 9, 2, 3, 18, 0, -1, 23, 2]
    want = sorted(a)
    sort.bubble_sort(a)
    assert a == want


def test_bubble_sort_odd():
    a = [1, 10, 9, 2, 3, 18, 0, -1, 23, 2, 12]
    want = sorted(a)
    sort.bubble_sort(a)
    assert a == want


def test_bubble_sort_big(big):
    big = big[:1000]
    want = sorted(big)
    sort.bubble_sort(big)
    assert big == want
