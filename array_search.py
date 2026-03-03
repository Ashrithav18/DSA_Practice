def searchStepArray(arr, k, x):
    n = len(arr)
    i = 0
    
    while i < n:
        if arr[i] == x:
            return i
        
        diff = abs(arr[i] - x)
        i += max(1, diff // k)
    
    return -1


# Example usage
print(searchStepArray([4,5,6,7,6], 1, 6))      # Output: 2
print(searchStepArray([20,40,50,70,70,60], 20, 60))  # Output: 5