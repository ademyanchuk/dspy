"""Sort Algorithms Implementations"""

from random import randint
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged


def quick_sort(arr: List[int], left: int, right: int):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)


def partition(arr: List[int], left: int, right: int) -> int:
    piv_idx = randint(left, right)
    piv_val = arr[piv_idx]
    # swap with last for convenience
    arr[piv_idx], arr[right] = arr[right], arr[piv_idx]
    # mem is split index, mem+1 will be pivot position
    # left is scanner index
    mem = left
    while left < right:
        if arr[left] > piv_val:
            left += 1
        else:
            arr[mem], arr[left] = arr[left], arr[mem]
            mem += 1
            left += 1
    # mem is the last index with element <= pivot
    arr[mem], arr[right] = arr[right], arr[mem]
    return mem


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        hold = arr[i]
        j = i - 1
        while (j > -1) and (hold < arr[j]):
            arr[j + 1] = arr[j]  # move right to find insertion place
            j -= 1
        # found insertion point
        arr[j + 1] = hold


def bubble_sort(arr: List[int]):
    for end in range(len(arr) - 1, 0, -1):
        for start in range(0, end):
            if arr[start] > arr[start + 1]:
                # bubble up
                arr[start], arr[start + 1] = arr[start + 1], arr[start]
