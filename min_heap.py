def heapify(arr, i, n):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # If left child exists and is smaller than root
    if l < n and arr[l] < arr[smallest]:
        smallest = l

    # If right child exists and is smaller than smallest so far
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    # If smallest is not root,
    # swap and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        # Recursively heapify
        heapify(arr, smallest, n)


if __name__ == "__main__":
    arr = [2, 3, 10, 4, 5, 1]

    # Print original array
    print("Original array: ", " ".join(str(x) for x in arr))

    # Build min-heap: perform heapify from last non-leaf node up to root
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))

   
    print("Min-Heap after heapify operation: ", " ".join(str(x) for x in arr))