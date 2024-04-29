import random
import time
import logging
import pytest

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def bubble_sort(arr):
    # ... (bubble sort implementation)
    return arr


def quick_sort(arr):
    # ... (quick sort implementation)
    return arr


@pytest.mark.parametrize("sort_function", [bubble_sort, quick_sort])
def test_sort_performance(sort_function):
    # Generate test data
    data = [random.randint(1, 10000) for _ in range(10000)]
    sorted_data = sorted(data)

    # Perform the sort and time it
    start_time = time.time()
    result = sort_function(data.copy())
    end_time = time.time()

    duration = end_time - start_time

    # Logging before assertion
    print(f"DEBUG: Starting logging for {sort_function.__name__}")
    logging.info(f"Time taken to sort with {sort_function.__name__}: {duration} seconds")
    print(f"DEBUG: Completed logging for {sort_function.__name__}")

    # Assert correct sorting for completeness
    assert result == sorted_data, "The sorting algorithm did not sort correctly."

    # Performance threshold assertion
    assert duration < 2, f"Sorting took too long with {sort_function.__name__}"


# Run the test directly when the script is executed standalone (not recommended for CI/CD)
if __name__ == "__main__":
    test_sort_performance(bubble_sort)
    test_sort_performance(quick_sort)
