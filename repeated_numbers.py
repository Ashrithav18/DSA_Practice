def repeatedNumber(arr):
    n = len(arr)
    
    # Expected sums
    sum_n = n * (n + 1) // 2
    sum_sq_n = n * (n + 1) * (2*n + 1) // 6
    
    # Actual sums
    S = sum(arr)
    P = sum(x*x for x in arr)
    
    # Differences
    x = S - sum_n              # A - B
    y = (P - sum_sq_n) // x    # A + B
    
    # Solve
    A = (x + y) // 2
    B = y - A
    
    return [A, B]


# Function Call
arr = [3, 1, 2, 5, 3]
print(repeatedNumber(arr))   # Output: [3, 4]