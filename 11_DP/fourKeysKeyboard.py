def maxA(n):
    dp = [0 for i in range(n+1)]

    for i in range(1, n+1):
        dp[i] = dp[i-1] + 1
        for j in range(1, i-3):
            dp[i] = max(dp[i], dp[j] * (i-j-1))
    
    return dp[n]

print(maxA(10))