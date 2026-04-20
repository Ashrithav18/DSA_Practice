def pairInSortedRotated(arr, target):
    n = len(arr)

    # Step 1: Find pivot (smallest element)
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i + 1
            break

    # Step 2: Initialize pointers
    left = pivot              # smallest
    right = (pivot - 1) % n   # largest

    # Step 3: Two pointer search
    while left != right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True

        elif current_sum < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False


# Function Calls
print(pairInSortedRotated([11, 15, 6, 8, 9, 10], 16))  # True
print(pairInSortedRotated([11, 11, 15, 26, 38, 9, 10], 35))  # True
print(pairInSortedRotated([9, 10, 10, 11, 15, 26, 38], 45))  # False