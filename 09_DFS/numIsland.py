# https://leetcode.cn/problems/number-of-islands/

def numIsland(grid):
    ans = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                ans += 1
                dfs(grid, i, j)
    return ans

def dfs(grid, i, j):
    if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
        return
    if grid[i][j] != 1:
        return
    
    grid[i][j] = 0
    dfs(grid, i-1, j)
    dfs(grid, i+1, j)
    dfs(grid, i, j-1)
    dfs(grid, i, j+1)


if __name__ == "__main__":
    grid = [
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]
    ]
    print(numIsland(grid))