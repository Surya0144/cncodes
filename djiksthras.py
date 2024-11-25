import heapq
import sys

def dijkstra(n, adj, src):
    dist = [sys.maxsize] * n
    dist[src] = 0

    pq = []
    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for weight, v in adj[u]:
            newDist = dist[u] + weight
            if newDist < dist[v]:
                dist[v] = newDist
                heapq.heappush(pq, (dist[v], v))

    print(f"Shortest distances from source node {src}:")
    for i in range(n):
        print(f"Node {i} : ", end="")
        if dist[i] == sys.maxsize:
            print("Unreachable")
        else:
            print(dist[i])

if __name__ == "__main__":
    n = 5
    adj = [[] for _ in range(n)]

    adj[0].append((10, 1))
    adj[0].append((3, 2))
    adj[1].append((1, 2))
    adj[1].append((2, 3))
    adj[2].append((4, 3))
    adj[3].append((2, 4))
    adj[2].append((8, 4))

    src = 0
    dijkstra(n, adj, src)
