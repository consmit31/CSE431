import copy

N, M, K = map(int, input().split())

G = {i : [] for i in range(N)}
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

terminals = set()
for i in range(K):
    terminals.add(int(input))

print(G)


# G - Graph
# N - Number of vertices in graph

def MST(G, N):
    mstSet = set()
    key = {i: float('inf') for i in range(N)}
    parent = {i: None for i in range(N)}

    key[0] = 0
    while len(mstSet) != N:
        # Find the vertex with the minimum key value from the set of vertices not yet included in MST
        u = min((v for v in range(N) if v not in mstSet), key=lambda x: key[x])
        mstSet.add(u)
        
        # Update key and parent values for vertices adjacent to u
        for v in G[u]:
            if v not in mstSet and 1 < key[v]:
                key[v] = 1
                parent[v] = u

    adjacency_map = {i: [] for i in range(N)}
    for v in range(N):
        if parent[v] is not None:
            adjacency_map[parent[v]].append(v)
            adjacency_map[v].append(parent[v])

    return adjacency_map

def is_valid_output(graph, K):
    def is_connected(graph):
        visited = set()
        stack = [0]
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                stack.extend(neighbor for neighbor in graph[v] 
                              if neighbor not in visited)
        return len(visited) == len(graph)
    
    def is_acyclic(graph):
        visited = set()
        stack = [i for i in range(N)]
        while stack:
            v = stack.pop()
            if v in visited:
                return False
            visited.add(v)
            stack.extend(neighbor for neighbor in graph[v]
                          if neighbor not in visited)
        return True
    

    if not is_connected(graph):
        return False
    
    if not is_acyclic(graph):
        return False
    
    for v in K:
        if v not in graph.keys():
            return False
            
    return True

def cost(graph):
    return sum(len(neighbors) for neighbors in graph.values()) // 2

best = G     
curr = set()
def solve(items, curr : set, K):  
    global best   
    if not items:           
        if is_valid_output(curr, K) and cost(curr) < cost(best):
            best = copy.deepcopy(curr)
    else:
        x = items.pop()
        solve(items, curr, K)
        solve(items, curr.add(x), K)
        

G = { 0 : [1, 4, 2],
      1 : [0, 4], 
      2 : [0, 4, 3],
      3 : [2],
      4 : [0, 1, 2] }
K = {0, 3}
items = {1, 2, 4} # All nodes not needed

print(solve(items, G, K))