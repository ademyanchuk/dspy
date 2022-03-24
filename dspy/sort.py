"""Sort Algorithms Implementations"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    pass
