def two_sum(arr,target):
    seen={}
    for i in range(len(arr)):
        diff = target - arr[i]
        
        if diff in seen:
            return [seen[diff], i]
        
        seen[arr[i]] = i
        
arr=[2,7,11,15]
target=9
print(two_sum(arr,target))