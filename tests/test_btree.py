import pytest

from dspy.bstree import BSTree


def test_dtype_is_none():
    tree = BSTree()
    assert tree._dtype is None


def test_dtype_set():
    val = 1
    tree = BSTree()
    tree._dtype = val
    assert tree._dtype == type(val)


def test_dtype_reassign():
    n, s = 1, "123"
    tree = BSTree()
    tree._dtype = n
    tree._dtype = s
    assert tree._dtype == type(n)


def test_check_type_raise_not_comparable():
    tree = BSTree()

    class Dummy:
        pass

    d = Dummy()
    with pytest.raises(AttributeError, match="comparable"):
        tree._check_dtype(d)


def test_check_dtype_mismatch():
    tree = BSTree()
    tree._dtype = 1
    with pytest.raises(AttributeError, match="mismatch"):
        tree._check_dtype_mismatch("123")


def test_insert():
    tree = BSTree()
    root = 123
    tree.insert(root)
    assert tree.root.val == root
    left = 12
    tree.insert(left)
    assert tree.root.left.val == left
