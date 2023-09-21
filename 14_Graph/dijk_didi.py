import heapq

def dijkstra(G):
    m, n = len(G), len(G[0])
    vis = []
    dist = []
    for _ in range(m):
        line = [False for _ in range(n)]
        vis.append(line)
        line = [float('inf') for _ in range(n)]
        dist.append(line)
    
    pq = [(0, [0, 0])]
    dist[0][0] = 0
    while pq:
        dis, cur = heapq.heappop(pq)
        i, j = cur[0], cur[1]
        if vis[i][j]:
            continue
        vis[i][j] = True
        if i > 0 and not vis[i-1][j]:
            w = G[i-1][j]
            dist[i-1][j] = min(dis + w, dist[i-1][j])
            heapq.heappush(pq, (dist[i-1][j], [i-1, j]))
        if i < m-1 and not vis[i+1][j]:
            w = G[i+1][j]
            dist[i+1][j] = min(dis + w, dist[i+1][j])
            heapq.heappush(pq, (dist[i+1][j], [i+1, j]))
        if j > 0 and not vis[i][j-1]:
            w = G[i][j-1]
            dist[i][j-1] = min(dis + w, dist[i][j-1])
            heapq.heappush(pq, (dist[i][j-1],[i, j-1]))
        if j < n-1 and not vis[i][j+1]:
            w = G[i][j+1]
            dist[i][j+1] = min(dis + w, dist[i][j+1])
            heapq.heappush(pq, (dist[i][j+1], [i, j+1]))
    return dist[m-1][n-1]

if __name__ == "__main__":
    m, n = map(int, input().split())
    G = []
    for _ in range(m):
        line = input().split()
        line = [int(s) for s in line]
        G.append(line)
    print(dijkstra(G))
