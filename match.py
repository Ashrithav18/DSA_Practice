def match(wild, pattern):
    n = len(wild)
    m = len(pattern)

    # DP table
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Empty matches empty
    dp[0][0] = True

    # Handle '*' matching empty string
    for i in range(1, n + 1):
        if wild[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if wild[i - 1] == pattern[j - 1] or wild[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]

            elif wild[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

            else:
                dp[i][j] = False

    return dp[n][m]


# Test
print(match("ge*ks", "geeks"))              # True
print(match("ge?ks*", "geeksforgeeks"))     # True
print(match("a*b", "ac"))                   # False