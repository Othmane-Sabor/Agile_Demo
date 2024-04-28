import random
import time
import pytest
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        greater = [x for x in arr if x >= pivot]
        lesser = [x for x in arr if x < pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


@pytest.mark.parametrize("sort_function", [bubble_sort, quick_sort])
def test_sort_performance(sort_function):
    data = [random.randint(1, 10000) for _ in range(1000)]
    sorted_data = sorted(data)

    start_time = time.time()
    assert sort_function(data.copy()) == sorted_data
    end_time = time.time()

    duration = end_time - start_time
    logging.info(f"Time taken to sort with {sort_function.__name__}: {duration} seconds")

    # Performance threshold example
    assert duration < 2, f"Sorting took too long with {sort_function.__name__}"
