import heapq
from typing import List, Set, Tuple


def dfs_visit_list(
    i: int, adj_list: List[List[int]], ans: List[int], visited: Set[int]
):
    if i in visited:
        return
    visited.add(i)
    for node in adj_list[i]:
        dfs_visit_list(node, adj_list, ans, visited)
    ans.append(i)


def dfs_list(adj_list: List[List[int]]) -> List[int]:
    visited = set()
    ans = []
    for i in range(len(adj_list)):
        dfs_visit_list(i, adj_list, ans, visited)
    return ans


def dfs_visit_list_iter(
    i: int, adj_list: List[List[int]], visited: Set[int]
) -> List[int]:
    stack = [i]
    ans = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            ans.append(node)
            for kid in adj_list[node]:
                if kid not in visited:
                    stack.append(kid)
    return list(reversed(ans))


def dfs_list_iter(adj_list: List[List[int]]) -> List[int]:
    visited = set()
    ans = []
    for i in range(len(adj_list)):
        if i not in visited:
            ans.extend(dfs_visit_list_iter(i, adj_list, visited))
    return ans


"""
Dijkstra Single Source Shortest Path Algorithm

Requirement: Weighted graph, no cycles with negative edges.

Concrete implementation assuming adjacency list with index i of the list = vertex from and adj[i] is a list of pairs of
integers to represent "vertices to" and weights (u -> v).

The implementation returns a 2 lists the same size as the adjacency list "distances" and "parents",
where every row i in the output represents the information about i-th vertex.
"Distances"[i] = sum of the weights of the shortest weighted path from 'start' to vertex[i].
"Parents"[i] = parent of the vertex[i] on this path from "start" to vertex[i].
Parent of "start" is -1. Parent information is required when we want to reconstruct
the exact shortest path from "start" to some vertex "x". For those vertices, which are not connected to "start",
result will be [inf], [-1]

"""


def dijkstra(adj: List[List[Tuple[int, int]]], s: int) -> Tuple[List[float], List[int]]:
    if not adj or s >= len(adj):
        raise ValueError
    n = len(adj)
    dist = [float("inf")] * n
    dist[s] = 0
    parent = [-1] * n
    visited = set()
    pq = [[0, s]]
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                parent[v] = u
                heapq.heappush(pq, [dist[v], v])
    return dist, parent


if __name__ == "__main__":
    adj_list = [
        [5, 3],
        [3],
        [2, 0],
        [0, 1],
        [],
        [2],
    ]
    ans = [2, 5, 1, 3, 0, 4]
    got = dfs_list(adj_list)
    assert got == ans, print(f"dfs_list: {got=} != {ans=}")

    got = dfs_list_iter(adj_list)
    assert got == ans, print(f"dfs_list_iter: {got=} != {ans=}")
