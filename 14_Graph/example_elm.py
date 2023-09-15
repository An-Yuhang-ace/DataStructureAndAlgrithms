import heapq

def djikstra(G, n):
    pq = [(0, 1)]
    visited = [False for _ in range(n+1)]
    dist = [float('inf') for _ in range(n+1)]
    dist[1] = 0

    while pq:
        dis, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and dist[v] > dis + w:
                dist[v] = dis + w
                heapq.heappush(pq, (dist[v], v))
    return dist

if __name__ == "__main__":
    # initialize and input
    n, m, q = map(int, input().split())
    G = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))
    
    a = [int(s) for s in input().split()]

    # dijkstra
    dist = djikstra(G, n)

    ans = 0
    for i in a:
        ans += dist[i] * 2
    
    print(ans)

