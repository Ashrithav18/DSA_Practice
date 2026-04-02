def maxSumPair(arr, k):
    arr.sort()
    n = len(arr)
    i = n - 1
    total_sum = 0
    
    while i > 0:
        # check difference
        if arr[i] - arr[i-1] < k:
            total_sum += arr[i] + arr[i-1]
            i -= 2   # skip both elements
        else:
            i -= 1   # move one step left
    
    return total_sum


# Function Call
arr = [3, 5, 10, 15, 17, 12, 9]
k = 4
print(maxSumPair(arr, k))