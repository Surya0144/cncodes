import heapq

def primMST(n, adj):
    key = [float('inf')] * n
    parent = [-1] * n
    inMST = [False] * n

    pq = [(0, 0)]
    key[0] = 0

    while pq:
        weight, u = heapq.heappop(pq)

        if inMST[u]:
            continue
        inMST[u] = True

        for v, w in adj[u]:
            if not inMST[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(pq, (key[v], v))

    total_cost = 0
    print("Edges in the MST:")
    for v in range(1, n):
        if parent[v] != -1:
            print(f"{parent[v]} - {v} : {key[v]}")
            total_cost += key[v]
        else:
            print(f"Node {v} is disconnected and not included in the MST.")
    print(f"Total cost of MST: {total_cost}")

if __name__ == "__main__":
    n = 5
    adj = [[] for _ in range(n)]
    adj[0].append((1, 10))
    adj[1].append((0, 10))
    adj[0].append((2, 6))
    adj[2].append((0, 6))
    adj[0].append((3, 5))
    adj[3].append((0, 5))
    adj[1].append((3, 15))
    adj[3].append((1, 15))
    adj[2].append((3, 4))
    adj[3].append((2, 4))

    primMST(n, adj)