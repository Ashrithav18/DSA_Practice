def permutationCoeff(n, k):
    # create dp table
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k) + 1):
            
            # base case
            if j == 0:
                dp[i][j] = 1
            
            else:
                dp[i][j] = dp[i-1][j] + j * dp[i-1][j-1]

    return dp[n][k]


# ----------- MAIN PROGRAM -----------

n = int(input("Enter n: "))
k = int(input("Enter k: "))

print("Permutation Coefficient:", permutationCoeff(n, k))