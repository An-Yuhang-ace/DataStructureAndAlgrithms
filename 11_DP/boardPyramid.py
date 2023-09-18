def DP(array):
    # DP: 以当前为底，所能垒加的最大高度 
    dp = [1 for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            if array[i][1] >= array[j][1]:
                dp[i] = max(dp[j]+1, dp[j])
        ans = max(ans, dp[i])
    return ans

if __name__ == "__main__":

    n = int(input().split()[0])
    line  = input().split()
    l = [int(s) for s in line]
    line  = input().split()
    w = [int(s) for s in line]

    array = []
    for i in range(n):
        array.append([l[i], w[i]])

    # double sort
    array.sort(key=lambda e:e[1])
    array.sort(key=lambda e:e[0])

    print(DP(array))

