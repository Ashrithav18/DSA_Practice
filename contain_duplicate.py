def contain_duplicate(nums):
    seen=set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums=[1,2,3,4,5]
result=contain_duplicate(nums)
print(result)