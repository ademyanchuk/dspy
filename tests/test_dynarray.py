import pytest

from dspy.dyn_array import DynamicArray


def test_init_empty():
    a = DynamicArray()
    assert len(a) == 0


def test_init_values():
    a = DynamicArray(val=(1, 2))
    assert len(a) == 2


def test_normalize_index():
    a = DynamicArray(val=(1, 2, 3))
    # -1 is 1 from the end, -2 second from the end etc
    assert a._normalize_idx(-3) == 0
    assert a._normalize_idx(-2) == 1


def test_get():
    a = DynamicArray(val=(2, 3))
    assert a[0] == 2


def test_get_negative():
    a = DynamicArray(val=(2, 3))
    assert a[-2] == 2


def test_set():
    a = DynamicArray(val=("a", "b", 5))
    a[2] = "c"
    assert a[2] == "c"


def test_out_of_range():
    a = DynamicArray()
    with pytest.raises(IndexError, match="out of range"):
        a._raise_if_out_range(0)


def test_out_of_range_negative():
    a = DynamicArray(val=(1, 2))
    with pytest.raises(IndexError, match="out of range"):
        a._raise_if_out_range(-5)


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


def test_append_with_resize():
    a = DynamicArray(val=(1,))
    init_cap = a._cap
    a.append(2)
    a.append(3)
    assert a._cap == init_cap * 2


def test_insert():
    idx = 1
    val = 2
    a = DynamicArray(val=(1, 10, 3))
    size = len(a)
    a.insert(idx=idx, val=val)
    assert a[idx] == val and len(a) == size + 1
