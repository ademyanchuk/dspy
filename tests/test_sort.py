import random

import pytest

from dspy import sort


@pytest.fixture(scope="module")
def big():
    return random.sample(range(1_000_000), k=999_000)


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
