def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


# Example list of elements
elements = [4, 8, 2, 7, 19, 22, 3, 5, 9]

print("Original list:", elements)

# Perform heap sort
heap_sort(elements)

print("Sorted list:", elements)

'''
output:

Original list: [4, 8, 2, 7, 19, 22, 3, 5, 9]
Sorted list: [2, 3, 4, 5, 7, 8, 9, 19, 22]

'''