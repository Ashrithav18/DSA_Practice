def findCeiling(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid   # Exact match is also ceiling
        
        elif arr[mid] < x:
            low = mid + 1
        
        else:
            result = mid   # Possible ceiling
            high = mid - 1
    
    return result
print(findCeiling([1,2,3,4],3))