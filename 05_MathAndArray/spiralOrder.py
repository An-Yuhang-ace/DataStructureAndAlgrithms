# https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/description/

def spiralOrder(matrix):
    m, n = len(matrix), len(matrix[0])
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    index = 0
    ans = []
    vis = []
    for i in range(m):
        line = [0 for _ in range(n)]
        vis.append(line)
    
    i, j = 0, 0
    while not vis[i][j]:
        ans.append(matrix[i][j])
        vis[i][j] = 1
        cur_direc = directions[index]
        if i+cur_direc[0] >= m or i+cur_direc[0] < 0 or j+cur_direc[1] >= n or j+cur_direc[1] < 0 or vis[i+cur_direc[0]][j+cur_direc[1]]:
            index = (index + 1) % 4
            cur_direc = directions[index]
        i += cur_direc[0]
        j += cur_direc[1]
    return ans


if __name__ == "__main__":
    matrix = [
        [1,2,3,4], 
        [5,6,7,8], 
        [9,10,11,12]
    ]
    print(spiralOrder(matrix))