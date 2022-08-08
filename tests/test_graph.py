import pytest

from dspy.graph import dijkstra


def test_ont():
    adj = [[(0, 0)]]
    s = 0
    dist, parent = dijkstra(adj, s)
    assert (dist, parent) == ([0], [-1])


def test_error_input():
    adj = [[(0, 0)]]
    s = 10
    with pytest.raises(ValueError):
        _, _ = dijkstra(adj, s)
    adj = []
    s = 0
    with pytest.raises(ValueError):
        _, _ = dijkstra(adj, s)


def test_complex():
    adj = [
        [(1, 3), (2, 1)],
        [(3, 10), (4, 2)],
        [(1, 1)],
        [(4, 2), (0, 3)],
        [(3, 2)],
        [(6, 1)],
        [(5, 1)],
    ]
    s = 0
    got = dijkstra(adj, s)
    want = ([0, 2, 1, 6, 4, float("inf"), float("inf")], [-1, 2, 0, 4, 1, -1, -1])
    assert got == want
