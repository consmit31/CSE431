id_x = input().split()
N = int(id_x[0])
M = int(id_x[1])

G = {}
for _ in range(M):
    agents = input().split()
    ag1 = int(agents[0])
    ag2 = int(agents[1])

    if ag1 not in G:
        G[ag1] = [ag2]
    else:
        G[ag1].append(ag2)

    if ag2 not in G:
        G[ag2] = [ag1]
    else:
        G[ag2].append(ag1)


def dfs(G, v, visited):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            dfs(G, u, visited)

visited = [0] * N
count = 0
for v in range(N):
    if not visited[v]:
       dfs(G, v, visited)
       count += 1

print(count)