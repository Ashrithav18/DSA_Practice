def minSum(a, b):

    a.sort()
    b.sort()

    total = 0

    for i in range(len(a)):
        total += abs(a[i] - b[i])

    return total


# Function Call
a = [4,1,8,7]
b = [2,3,6,5]

print(minSum(a,b))