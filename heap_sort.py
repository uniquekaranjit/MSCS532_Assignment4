# ----------------------------------------------------------------------------------------------------------------------
# Driver Code to implememt heap sort. 
# Author: Unique Karanjit
# Jan 25, 2025
# ----------------------------------------------------------------------------------------------------------------------

def heapify(arr, n, i):
    """
    Maintains the heap property for a subtree rooted at index i.
    :param arr: List of elements
    :param n: Size of the heap
    :param i: Index of the root of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Implements Heapsort algorithm to sort an array.
    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    n = len(arr)

    # Step 1: Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum element) with the last element
        arr[i], arr[0] = arr[0], arr[i]
        # Reduce the heap size and maintain the heap property
        heapify(arr, i, 0)

    return arr


# ----------------------------------------------------------------------------------------------------------------------
# Driver Code
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Original array:", array)
    sorted_array = heap_sort(array)
    print("Sorted array:", sorted_array)
