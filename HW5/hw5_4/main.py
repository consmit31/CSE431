id_x = input().split()
N = int(id_x[0])
M = int(id_x[1])

G = {}
for _ in range(M):
    abl = input().split()
    a = int(abl[0])
    b = int(abl[1])
    w = int(abl[2])

    if a not in G:
        G[a] = [[b,w]]
    else:
        G[a].append([b,w])

    if b not in G:
        G[b] = [[a,w]]
    else:
        G[b].append([a,w])

def find(component, u):
    if component[u] != u:
        component[u] = find(component, component[u])
    return component[u]

e = []
for n in G:
    for v, w in G[n]:
        e.append((n, v, w))
e.sort(key=lambda x: x[2])
component = {node: node for node in G}
rank = {node: 0 for node in G}
total = 0
for u, v, w in e:
    if find(component, u) != find(component, v):
        u_root = find(component, u)
        v_root = find(component, v)
        if rank[u_root] < rank[v_root]:
            component[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            component[v_root] = u_root
        else:
            component[v_root] = u_root
            rank[u_root] += 1
        total += w

print(total)