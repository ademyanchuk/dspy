import pytest

from dspy.linked_list import LinkedList, ListNode


def test_node_repr():
    n = ListNode(1)
    assert repr(n) == "ListNode(value=1, next=None)"


def test_node_str():
    node = ListNode(1)
    assert str(node) == "1"


def test_init_tail():
    llist = LinkedList(1)
    assert llist.tail is not None
    assert llist.head == llist.tail


def test_list_len_empty():
    llist = LinkedList()
    assert not llist


def test_list_len_one():
    llist = LinkedList("a")
    assert len(llist) == 1


def test_list_repr_empty():
    llist = LinkedList()
    assert repr(llist) == "LinkedList(value=None)"


def test_list_repr_one():
    llist = LinkedList(1)
    assert repr(llist) == "LinkedList(value=1)"


def test_list_str_one():
    llist = LinkedList(1)
    assert str(llist) == "LinkedList([1])"


def test_list_get_item_err():
    llist = LinkedList()
    with pytest.raises(IndexError, match="out of range"):
        llist[0]
    with pytest.raises(IndexError, match="out of range"):
        llist[-1]


def test_list_get_item_zero():
    llist = LinkedList(1)
    n = llist[0]
    if n is not None:
        assert n.data == 1


def test_list_set_item_err():
    llist = LinkedList()
    with pytest.raises(IndexError, match="out of range"):
        llist[0] = 1


def test_list_set_item_zero():
    llist = LinkedList(1)
    llist[0] = 123
    n = llist[0]
    if n is not None:
        assert n.data == 123


def test_list_del_item_err():
    llist = LinkedList(1)
    with pytest.raises(IndexError, match="out of range"):
        llist[1]
    with pytest.raises(IndexError, match="out of range"):
        llist[-2]


def test_list_del_item_first():
    llist = LinkedList(1)
    llist.push_back(2)
    del llist[0]
    assert len(llist) == 1
    assert str(llist[0]) == "2"


def test_list_del_item_last():
    llist = LinkedList(1)
    llist.push_back(2)
    del llist[-1]
    assert len(llist) == 1
    assert str(llist[-1]) == "1"


def test_list_del_item_middle():
    llist = LinkedList(1)
    llist.push_back(2)
    llist.push_back(3)
    del llist[1]
    assert len(llist) == 2
    assert llist.head is not None
    assert llist.tail is not None
    assert llist.head != llist.tail
    assert str(llist) == "LinkedList([1,3])"


def test_list_push_front():
    llist = LinkedList(1)
    llist.push_front(2)
    head = llist.head
    assert head is not None and head.data == 2


def test_list_push_front_one():
    # head and tail should be the same
    llist = LinkedList()
    llist.push_front(1)
    assert llist.head is not None
    assert llist.head == llist.tail


def test_list_push_front_two():
    # head and tail should be the same
    llist = LinkedList()
    llist.push_front(1)
    llist.push_front(2)
    assert llist.head is not None
    assert llist.head != llist.tail


def test_list_pop_front_raise():
    llist = LinkedList()
    with pytest.raises(IndexError, match="empty linked list"):
        llist.pop_front()


def test_list_pop_front_ok():
    llist = LinkedList(1)
    llist.push_front(2)
    val = llist.pop_front()
    assert len(llist) == 1 and llist.head.data == 1 and val == 2


def test_list_pop_front_last_node():
    # then we poped last node both head and tail
    # should be None
    llist = LinkedList(1)
    llist.push_front(2)
    _ = llist.pop_front()
    _ = llist.pop_front()
    assert llist.head is None
    assert llist.tail is None


def test_list_push_back_one():
    # head and tail should be the same
    llist = LinkedList()
    llist.push_back(1)
    assert llist.head is not None
    assert llist.head == llist.tail


def test_list_push_back_two():
    # head and tail should be the same
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    assert llist.head is not None
    assert llist.head != llist.tail


def test_list_push_front_and_back():
    llist = LinkedList()
    llist.push_front(1)
    llist.push_back(2)
    assert str(llist) == "LinkedList([1,2])"


def test_list_pop_back_raise():
    llist = LinkedList()
    with pytest.raises(IndexError, match="empty linked list"):
        llist.pop_back()


def test_list_pop_back_ok():
    llist = LinkedList(1)
    llist.push_back(2)
    _ = llist.pop_back()
    assert str(llist) == "LinkedList([1])"


def test_list_pop_back_last_node():
    # then we poped last node both head and tail
    # should be None
    llist = LinkedList(1)
    llist.push_back(2)
    _ = llist.pop_back()
    _ = llist.pop_back()
    assert llist.head is None
    assert llist.tail is None


def test_list_peek_raise():
    llist = LinkedList()
    with pytest.raises(IndexError, match="empty linked list"):
        llist.peek_front()
    with pytest.raises(IndexError, match="empty linked list"):
        llist.peek_back()


def test_list_peek_front():
    llist = LinkedList(1)
    llist.push_front(2)
    assert llist.peek_front() == 2


def test_list_peek_back():
    llist = LinkedList(1)
    llist.push_back(2)
    assert llist.peek_back() == 2


def test_list_insert_out_index_back():
    # idx == len and positive
    llist = LinkedList(1)
    llist.push_back(2)
    llist.insert(2, 3)
    assert len(llist) == 3
    assert str(llist) == "LinkedList([1,2,3])"


def test_list_insert_out_index_front():
    # normilized idx == 0
    llist = LinkedList(1)
    llist.push_back(2)
    llist.insert(-2, 3)
    assert len(llist) == 3
    assert str(llist) == "LinkedList([3,1,2])"


def test_list_insert_in_range_positive():
    # before last
    llist = LinkedList(1)
    for i in range(2, 5):
        llist.push_front(i)

    length = len(llist)
    idx = length - 1
    llist.insert(idx, 10)
    assert len(llist) == length + 1
    assert llist[idx].data == 10


def test_list_insert_in_range_negative():
    # before last
    llist = LinkedList(1)
    for i in range(2, 5):
        llist.push_front(i)

    length = len(llist)
    llist.insert(-3, 10)  # -3 is index 1 for current list
    assert len(llist) == length + 1
    assert llist[-4].data == 10  # -4 is index 1 for updated list


def test_reverse():
    llist = LinkedList()
    for i in range(5):
        llist.push_front(i)
    llist.reverse()
    assert str(llist) == "LinkedList([0,1,2,3,4])"


def test_reverse_one():
    llist = LinkedList(1)
    llist.reverse()
    assert llist.head == llist.tail
