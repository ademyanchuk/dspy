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


def test_delete_midle():
    a = DynamicArray(val=(1, 2, 3))
    idx = 1
    size = len(a)
    del a[idx]
    assert a[idx] != 2 and len(a) == size - 1


def test_delete_first():
    a = DynamicArray(val=(1, 2, 3))
    idx = 0
    size = len(a)
    del a[idx]
    assert a[idx] != 1 and len(a) == size - 1


def test_delete_last():
    a = DynamicArray(val=(1, 2, 3))
    idx = -1
    size = len(a)
    del a[idx]
    assert a[idx] != 3 and len(a) == size - 1


def test_contains():
    a = DynamicArray(val=(1, 3.3, "222"))
    assert 3.3 in a


def test_not_find():
    a = DynamicArray()
    assert a.find("abc") == -1


def test_find():
    a = DynamicArray(val=(1, "abc", 3.4))
    assert a.find("abc") == 1


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


def test_prepend():
    val = 0
    a = DynamicArray(val=(1,))
    a.prepend(val)
    assert a[0] == val


def test_pop():
    a = DynamicArray(val=[1, 2, 3])
    last = a[-1]
    size = len(a)
    got = a.pop()
    assert last == got and len(a) == size - 1


def test_pop_raises():
    a = DynamicArray()
    with pytest.raises(IndexError, match="empty list"):
        a.pop()


def test_no_remove():
    a = DynamicArray(val=(1, 2, 3))
    old_size = len(a)
    a.remove(4)
    assert len(a) == old_size
    assert str(a) == "DynamicArray([1,2,3])"


def test_remove_two():
    a = DynamicArray(val=(1, 2, 3, 2, 4))
    old_size = len(a)
    a.remove(2)
    print(a)
    assert len(a) == old_size - 2
    assert 2 not in a
    assert str(a) == "DynamicArray([1,3,4])"


def test_remove_three():
    a = DynamicArray(val=(3, 1, 3, 2, 4, 3))
    old_size = len(a)
    a.remove(3)
    print(a)
    assert len(a) == old_size - 3
    assert 3 not in a
    assert str(a) == "DynamicArray([1,2,4])"


def test_maybe_shrink():
    a = DynamicArray(val=(1,))
    a._resize(8)
    big_cap = a._cap
    # now len is 1, cap is 8
    a._maybe_shrink()
    assert a._cap == big_cap // 2
