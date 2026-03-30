def maxSubstring(S):
    max_sum = 0
    curr_sum = 0
    
    for ch in S:
        if ch == '0':
            val = 1
        else:
            val = -1
        
        curr_sum = max(val, curr_sum + val)
        max_sum = max(max_sum, curr_sum)
    
    # If all are 1s
    if max_sum == 0:
        return -1
    
    return max_sum


# Example
print(maxSubstring("11000010001"))  # Output: 6
print(maxSubstring("111111"))       # Output: -1