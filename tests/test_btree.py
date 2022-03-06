import pytest

from dspy.bstree import BSTree, find_by_value, level_traverse


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


def test_init_from_values():
    tree = BSTree(values=[2, 1, 3])
    assert tree.root.val == 2 and tree.root.left.val == 1 and tree.root.right.val == 3


def test_level_traverse():
    tree = BSTree()
    values = [2, 3, 1]
    want = [2, 1, 3]
    for v in values:
        tree.insert(v)
    got = level_traverse(tree.root)
    assert got == want


def test_level_traverse_larger():
    tree = BSTree()
    want = [4, 2, 7, 1, 3, 6, 9]
    for v in want:
        tree.insert(v)
    got = level_traverse(tree.root)
    assert got == want


def test_level_traverse_empty():
    tree = BSTree()
    got = level_traverse(tree.root)
    assert not got


def test_find_by_value_none():
    tree = BSTree()
    tree.insert(20)
    tree.insert(10)
    assert find_by_value(tree.root, 5) is None


def test_find_by_value():
    tree = BSTree()
    tree.insert(20)
    tree.insert(10)
    tree.insert(30)
    node = find_by_value(tree.root, 10)
    assert node is not None and node == tree.root.left


def test_inorder():
    values = [4, 3, 9, 1, 12, 2, 0]
    tree = BSTree(values)
    got = tree.inorder()
    assert got == sorted(values)


def test_find_empty():
    tree = BSTree()
    assert tree.find(123) is None


def test_find_incompatible():
    tree = BSTree(values=[1, 2, 3])
    assert tree.find("abc") is None


def test_find_valid():
    tree = BSTree(values=[1, 2, 3, -1, -2])
    assert tree.find(1).val == 1
