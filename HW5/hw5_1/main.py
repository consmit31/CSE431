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
        if len(graph[a]) > max:
            max = len(graph[a])
            agent = a

    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
        if len(graph[b]) > max:
            max = len(graph[b])
            agent = b
    else:
        graph[b] = [a]

connections = int(((max + 1) * max) / 2)
print(connections)