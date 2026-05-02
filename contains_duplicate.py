def contain_duplicate(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

arr=[1,2,3,4,4,5,6,7,7,8]
print(contain_duplicate(arr))