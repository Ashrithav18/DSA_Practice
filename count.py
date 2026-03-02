def countingSort(arr):
    n = len(arr)
    max_val = max(arr)
    
    # Step 1: Create count array
    count = [0] * (max_val + 1)
    
    # Step 2: Count frequencies
    for num in arr:
        count[num] += 1
    
    # Step 3: Compute prefix sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Step 4: Build output array
    output = [0] * n
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output


# Example
print(countingSort([1,4,0,2,1,1]))