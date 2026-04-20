def maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        num = nums[i]
        
        # If negative, swap
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(num, num * max_prod)
        min_prod = min(num, num * min_prod)
        
        result = max(result, max_prod)
    
    return result


# Function Call
nums = [2,3,-2,4]
print(maxProduct(nums))   # Output: 6