def nextPermutation(arr):
    n = len(arr)

    # Step 1: Find breakpoint
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # Step 2: If found
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Swap
        arr[i], arr[j] = arr[j], arr[i]

    # Step 3: Reverse right side
    arr[i + 1:] = reversed(arr[i + 1:])

    return arr


# Test
print(nextPermutation([2, 4, 1, 7, 5, 0]))  # [2, 4, 5, 0, 1, 7]
print(nextPermutation([3, 2, 1]))           # [1, 2, 3]
print(nextPermutation([3, 4, 2, 5, 1]))     # [3, 4, 5, 1, 2]