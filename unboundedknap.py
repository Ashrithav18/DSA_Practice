def unboundedKnapsack(val, wt, capacity):
    n = len(val)
    
    # dp[i] = max profit for capacity i
    dp = [0] * (capacity + 1)
    
    # Build dp array
    for i in range(capacity + 1):
        for j in range(n):
            if wt[j] <= i:
                dp[i] = max(dp[i], val[j] + dp[i - wt[j]])
    
    return dp[capacity]


# Example
val = [10, 40, 50, 70]
wt = [1, 3, 4, 5]
capacity = 8

print(unboundedKnapsack(val, wt, capacity))  # Output: 110