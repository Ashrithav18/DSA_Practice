def findPair(arr, x):
    seen = set()
    
    for num in arr:
        if (num + x) in seen or (num - x) in seen:
            return "Yes"
        
        seen.add(num)
    
    return "No"


# Example
print(findPair([5, 20, 3, 2, 50, 80], 78))  # Yes
print(findPair([90, 70, 20, 80, 50], 45))   # No