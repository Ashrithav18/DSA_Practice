def maxSumPairWithDifferenceLessThanK(arr, n, k):
    arr.sort()
    i = n - 1
    total_sum = 0

    while i > 0:
        if arr[i] - arr[i-1] < k:
            total_sum += arr[i] + arr[i-1]
            i -= 2
        else:
            i -= 1

    return total_sum


# ----------- MAIN PROGRAM -----------

# Input
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))
n = len(arr)

# Function Call
result = maxSumPairWithDifferenceLessThanK(arr, n, k)

# Output
print("Maximum sum of pairs:", result)