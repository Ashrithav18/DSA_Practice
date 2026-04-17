def nextPermutation(nums):
    n = len(nums)
    
    # Step 1: find breaking point
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # Step 2: swap with next greater element
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 3: reverse remaining
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# -------- FUNCTION CALL --------
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)   # Output: [1, 3, 2]