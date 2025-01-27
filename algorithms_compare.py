# ----------------------------------------------------------------------------------------------------------------------
# Driver Code to compare heap sort, merge sort and quick sort. 
# Author: Unique Karanjit
# Jan 25, 2025
# ----------------------------------------------------------------------------------------------------------------------
import time
import numpy as np
import matplotlib.pyplot as plt
import sys

from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort



if __name__ == "__main__":
    # Increase recursion limit to handle larger inputs
    sys.setrecursionlimit(10**6)

    # Generate a sample array and compare sorting times
    array_sizes = [10, 100, 1000, 5000]
    merge_sort_times = []
    quick_sort_times = []
    heap_sort_times = []

    for size in array_sizes:
        sample_array = np.random.randint(0, 10000, size).tolist()
        sample_array = sorted(sample_array)

        # Merge Sort
        start_time = time.time()
        merge_sort(sample_array[:])
        merge_sort_times.append(time.time() - start_time)

        # Quick Sort
        start_time = time.time()
        quick_sort(sample_array[:])
        quick_sort_times.append(time.time() - start_time)

        # Heap Sort
        start_time = time.time()
        heap_sort(sample_array[:])
        heap_sort_times.append(time.time() - start_time)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, merge_sort_times, label="Merge Sort", marker="o")
    plt.plot(array_sizes, quick_sort_times, label="Quick Sort", marker="o")
    plt.plot(array_sizes, heap_sort_times, label="Heap Sort", marker="o")

    plt.title("Sorting Algorithm Performance Comparison")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()