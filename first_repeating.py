def repeating_num(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1
arr=[1,2,3,4,4,5,6,6]
print(repeating_num(arr))