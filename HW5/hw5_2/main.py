inp = input().split()
N = int(inp[0])
M = int(inp[1])

graph = {}
max = 0
agent = None
for _ in range(M):
    pair = input().split()
    a = int(pair[0])
    b = int(pair[1])

    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

max_connections = 0

for a in range(1, N + 1):
    if a in graph:
        for b in graph[a]:
            total_connections = len(set(graph[a] + graph[b]))
            if total_connections > max_connections:
                max_connections = total_connections

print(int(max_connections * (max_connections - 1) / 2))