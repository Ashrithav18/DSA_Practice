def mergeIntervals(arr):
    # Step 1: Sort intervals based on start time
    arr.sort()

    merged = []

    for interval in arr:
        # If merged list is empty OR no overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Overlapping → merge
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Function Calls
print(mergeIntervals([[1, 3], [2, 4], [6, 8], [9, 10]]))
print(mergeIntervals([[7, 8], [1, 5], [2, 4], [4, 6]]))