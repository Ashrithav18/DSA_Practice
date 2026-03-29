def countBT(h):
    dp = [0] * (h + 1)
    
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, h + 1):
        dp[i] = dp[i-1] * dp[i-1] + 2 * dp[i-1] * dp[i-2]
    
    return dp[h]


# Example
print(countBT(2))  # 3
print(countBT(3))  # 15