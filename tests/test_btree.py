import pytest

from dspy.bstree import (
    BSTree,
    TreeNode,
    _first,
    _is_leaf,
    _last,
    find_by_value,
    level_traverse,
)


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
    assert tree.insert(root)
    assert tree.root.val == root
    left = 12
    assert tree.insert(left)
    assert tree.root.left.val == left
    left = 13
    assert tree.insert(left)
    assert tree.root.left.right.val == left


def test_insert_mismatch():
    tree = BSTree(
        values=[
            2,
        ]
    )
    assert not tree.insert("a")


def test_insert_duplicate():
    tree = BSTree(values=[2, 1, 3])
    assert not tree.insert(2)


def test_del_value_mismatch():
    tree = BSTree(values=[2, 1, 3])
    assert not tree.del_value("a")


def test_del_value_not_present():
    tree = BSTree(values=[10, 3, 20])
    assert not tree.del_value(100)


def test_del_value_leaf():
    tree = BSTree(values=[5, 1, 12])
    assert tree.del_value(12)
    assert 12 not in tree


def test_del_value_left_child():
    tree = BSTree(values=[6, 4, 9, 2])
    assert tree.del_value(4)
    assert tree.inorder() == [2, 6, 9]


def test_del_value_right_child():
    tree = BSTree(values=[6, 4, 9, 5])
    assert tree.del_value(4)
    assert tree.inorder() == [5, 6, 9]


def test_del_value_two_children():
    tree = BSTree(values=[8, 3, 12, 10, 18, 17, 11, 9])
    assert tree.del_value(12)
    assert tree.inorder() == [3, 8, 9, 10, 11, 17, 18]


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


def test_in():
    tree = BSTree(values=[2, 1, 3])
    assert 3 in tree


def test_get_height():
    tree = BSTree(values=[3, 1, 4, 5])
    assert tree.height() == 2


def test_not_is_leaf():
    node = TreeNode(val=2)
    assert _is_leaf(node)


def test_is_leaf():
    node = TreeNode(val=2, left=TreeNode(3))
    assert not _is_leaf(node)


def test_is_leaf2():
    node = TreeNode(val=2, left=TreeNode(3), right=TreeNode(4))
    assert not _is_leaf(node)


def test_first_root():
    tree = BSTree(values=[1])
    node = _first(tree.root)
    assert node == tree.root


def test_first():
    tree = BSTree(values=[2, 1, 0])
    first = _first(tree.root)
    assert first == tree.root.left.left


def test_last():
    tree = BSTree(values=[0, 1, 2])
    last = _last(tree.root)
    assert last == tree.root.right.right


def test_min():
    tree = BSTree(values=[5, 2, 1, 30, 12, 19])
    assert tree.min() == 1


def test_max():
    tree = BSTree(values=[5, 2, 1, 30, 12, 19])
    assert tree.max() == 30


def test_get_node_count_empty():
    tree = BSTree()
    assert tree.get_node_count() == 0


def test_get_node_count_insert():
    vals = [4, 5, 1, 0, 3]
    tree = BSTree(values=vals)
    # duplicate will not be inserted
    tree.insert(5)
    assert tree.get_node_count() == len(vals)


def test_get_node_count_delete():
    vals = [4, 5, 1, 0, 3]
    tree = BSTree(values=vals)
    tree.del_value(5)
    # not in tree will not be deleted
    tree.del_value(5)
    assert tree.get_node_count() == len(vals) - 1


def test_delete():
    tree = BSTree([1, 2, 323, 12, 3])
    tree.delete()
    assert tree.root is None
    assert tree.get_node_count() == 0


def test_is_bstree_none():
    tree = BSTree()
    assert tree.is_bstree()


def test_is_bstree():
    tree = BSTree(values=[4, 1, 0, 22, 11, 2])
    tree.del_value(22)
    tree.insert(54)
    assert tree.is_bstree()


def test_not_is_bstree():
    tree = BSTree()
    node = TreeNode(val=5, left=TreeNode(1), right=TreeNode(10))
    node.right.right = TreeNode(1)
    tree.root = node
    assert not tree.is_bstree()
