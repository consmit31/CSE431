def convert(N, K, edges):
    new_K = N - K

    complement_edges = []
    for i in range(N):
        for j in range(i + 1, N):
            if (i, j) not in edges and (j, i) not in edges:
                complement_edges.append((i, j))

    print(N, len(complement_edges), new_K)
    for edge in complement_edges:
        print(edge[0], edge[1])

N, M, K = map(int, input().split())
edges = set()
for _ in range(M):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u  
    edges.add((u, v))

convert(N, K, edges)