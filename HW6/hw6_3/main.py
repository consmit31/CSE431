def is_valid_cycle(graph, cycle):
    visited = [False] * len(graph)

    if cycle[-1] not in graph[cycle[0]]:
        return False
    
    # Check if each edge in the cycle exists in the graph
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i + 1]
        if v not in graph[u]:
            return False
    
    # Check if each vertex is visited exactly once
    for vertex in cycle:
        if visited[vertex]:
            return False
        visited[vertex] = True
    
    # Check if the cycle loops back to the start
    if not visited[cycle[0]]:
        return False
    
    return True


N, M = map(int, input().split())
graph = {i: set() for i in range(N)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

T = int(input())
cycles = []
for _ in range(T):
    cycle = list(map(int, input().split()))
    cycles.append(cycle)

for c in cycles:
    if is_valid_cycle(graph, c):
        print("YES")
    else:
        print("NO") 

