from functools import cmp_to_key

def largestNumber(arr):
    
    # Convert numbers to string
    arr = list(map(str, arr))
    
    # Custom comparator
    def compare(x, y):
        if x + y > y + x:
            return -1   # x should come first
        elif x + y < y + x:
            return 1    # y should come first
        else:
            return 0
    
    # Sort using custom logic
    arr.sort(key=cmp_to_key(compare))
    
    # Edge case: if largest is "0"
    if arr[0] == "0":
        return "0"
    
    return ''.join(arr)


# Test
print(largestNumber([3, 30, 34, 5, 9]))     # 9534330
print(largestNumber([54, 546, 548, 60]))    # 6054854654