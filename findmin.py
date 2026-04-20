def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # minimum is in right part
            left = mid + 1
        else:
            # minimum is in left part
            right = mid
    
    return nums[left]


# Function Call
nums = [3,4,5,1,2]
print(findMin(nums))   # Output: 1