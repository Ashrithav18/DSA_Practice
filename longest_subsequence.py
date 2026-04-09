def longestSubsequence(arr):
    dp = {}
    max_len = 0
    
    for x in arr:
        dp[x] = 1 + max(dp.get(x-1, 0), dp.get(x+1, 0))
        max_len = max(max_len, dp[x])
    
    return max_len


# Function Call
arr = [10, 9, 4, 5, 4, 8, 6]
print(longestSubsequence(arr))