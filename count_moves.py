def count(n):
    dp = [0] * (n + 1)
    
    dp[0] = 1  # base case
    
    moves = [3, 5, 10]
    
    # Process each move
    for move in moves:
        for i in range(move, n + 1):
            dp[i] += dp[i - move]
    
    return dp[n]


# Example
print(count(10))  # Output: 2
print(count(20))  # Output: 4