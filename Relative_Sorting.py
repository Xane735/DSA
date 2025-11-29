import heapq

def relativeSort(arr1, arr2):
    # 1. Create a map for quick lookup of ranks (indices) in arr2
    # key: number, value: index in arr2
    rank_map = {val: i for i, val in enumerate(arr2)}
    
    # We use this as the rank for elements NOT in arr2
    # It ensures they appear after all arr2 elements
    end_rank = len(arr2)
    
    heap = []
    
    # 2. Build the Heap
    for num in arr1:
        if num in rank_map:
            # Tuple: (Index in arr2, value)
            # Sorting priority: Index first
            heapq.heappush(heap, (rank_map[num], num))
        else:
            # Tuple: (End Rank, value)
            # Sorting priority: End Rank (all same), then Value (ascending)
            heapq.heappush(heap, (end_rank, num))
            
    # 3. Extract from Heap
    res = []
    while heap:
        # We only need the value (the second item in tuple)
        _, val = heapq.heappop(heap)
        res.append(val)
        
    return res

def main():
    arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    arr2 = [2, 1, 8, 3]
    
    print("Original arr1:", arr1)
    print("Relative Order:", arr2)
    
    result = relativeSort(arr1, arr2)
    print("Sorted Result:", result)

if __name__ == "__main__":
    main()