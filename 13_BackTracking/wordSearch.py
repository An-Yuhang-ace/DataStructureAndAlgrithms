# https://leetcode.cn/problems/word-search/

def wordSearch(board, word):
    n = len(board)
    m = len(board[0])
    vis = []
    res = False
    for _ in range(n):
        line = [0 for _ in range(m)]
        vis.append(line)
    for i in range(n):
        for j in range(m):
            res = res or dfs(board, word, i, j, vis, 0)
    return res

def dfs(board, word, i, j, vis, index):
    res = False
    n = len(board)
    m = len(board[0])
    if word[index] != board[i][j]:
        return False
    elif index+1 >= len(word):
        return True
    
    
    vis[i][j] = 1
    if i > 0 and not vis[i-1][j]:
        res = res or dfs(board, word, i-1, j, vis, index+1)
    if i < n-1 and not vis[i+1][j]:
        res = res or dfs(board, word, i+1, j, vis, index+1)
    if j > 0 and not vis[i][j-1]:
        res = res or dfs(board, word, i, j-1, vis, index+1)
    if j < m-1 and not vis[i][j+1]:
        res = res or dfs(board, word, i, j+1, vis, index+1)
    vis[i][j] = 0
    return res

if __name__ == "__main__":
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    # board = [
    #     ["A"]
    # ]
    word = "ABC"
    print(wordSearch(board, word))