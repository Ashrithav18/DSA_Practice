def minMergeOperations(arr):
    i = 0
    j = len(arr) - 1
    count = 0

    while i < j:

        # Case 1: Equal → no merge
        if arr[i] == arr[j]:
            i += 1
            j -= 1

        # Case 2: Left smaller → merge left
        elif arr[i] < arr[j]:
            arr[i + 1] += arr[i]
            i += 1
            count += 1

        # Case 3: Right smaller → merge right
        else:
            arr[j - 1] += arr[j]
            j -= 1
            count += 1

    return count


# Test Cases
print(minMergeOperations([15, 4, 15]))   # 0
print(minMergeOperations([1, 4, 5, 1]))  # 1
print(minMergeOperations([11, 14, 15, 99]))  # 3