import sys

if __name__ == "__main__":
    # initialize the data structure
    g = []
    n, a, b = 0, 0, 0
    N = 1000
    for i in range(N+1):
        l = [0 for _ in range(N+1)]
        g.append(l)
    
    # input
    line = sys.stdin.readline()
    line = [int(s) for s in line.split()]
    n, a, b = line[0], line[1], line[2]
    a += 1
    b += 1
    for _ in range(n):
        line = sys.stdin.readline()
        x, y = int(line.split()[0]), int(line.split()[1])
        g[x][y] += 1

    # prefixSum calculate
    for i in range(1, N+1):
        for j in range(1, N+1):
            g[i][j] += g[i-1][j] + g[i][j-1] - g[i-1][j-1]

    # query in prefixSum matrix
    res = 0
    for i in range(a, N+1):
        for j in range(b, N+1):
            res = max(res, g[i][j] - g[i-a][j] - g[i][j-b] + g[i-a][j-b])
    print(res)

