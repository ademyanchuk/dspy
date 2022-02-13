import pytest

from dspy.dyn_array import DynamicArray


def test_init_empty():
    a = DynamicArray()
    assert len(a) == 0


def test_init_values():
    a = DynamicArray(val=(1, 2))
    assert len(a) == 2


def test_get():
    a = DynamicArray(val=(2, 3))
    assert a[0] == 2


def test_set():
    a = DynamicArray(val=("a", "b", 5))
    a[2] = "c"
    assert a[2] == "c"


def test_out_of_range():
    a = DynamicArray()
    with pytest.raises(IndexError, match="out of range"):
        a._raise_if_out_range(0)


def test_str():
    a = DynamicArray(val=(1, 2, 3))
    assert str(a) == "DynamicArray([1,2,3])"


def test_resize():
    v = (1, 2)
    new_cap = 8
    a = DynamicArray(val=v)
    a._resize(new_cap)
    assert a._cap == new_cap
    assert len(a) == len(v)
    assert str(a) == "DynamicArray([1,2])"


def test_append():
    a = DynamicArray(val=(1, 2))
    a.append(3)
    assert a[len(a) - 1] == 3
    assert len(a) == 3
