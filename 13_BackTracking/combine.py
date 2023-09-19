# https://leetcode.cn/problems/combinations/

ans = []
path = []

def combine(n, k):
    dfs(n, k, 1)
    return ans

def dfs(n, k, i):
    if len(path) == k:
        ans.append(path.copy())
        return
    for j in range(i, n+1):
        path.append(j)
        dfs(n, k, j+1)
        del path[-1]

if __name__ == "__main__":
    n = 4
    k = 2
    print(combine(n, k))