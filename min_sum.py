def minSum(arr):
    
    arr.sort()
    
    num1 = 0
    num2 = 0
    
    for i in range(len(arr)):
        if i % 2 == 0:
            num1 = num1 * 10 + arr[i]
        else:
            num2 = num2 * 10 + arr[i]
    
    return num1 + num2


# Function Call
arr = [6, 8, 4, 5, 2, 3]
print(minSum(arr))