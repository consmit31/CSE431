import copy

G = { 0 : {1, 4, 2},
      1 : {0, 4}, 
      2 : {0, 4, 3},
      3 : {2},
      4 : {0, 1, 2} }
K = {0, 3}
V = {0, 1, 2, 3, 4}
items = {1, 2, 4} # All nodes not needed

def cost(graph):
    return sum(len(neighbors) for neighbors in graph.values()) // 2

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
        stack = [i for i in range(len(graph))]
        while stack:
            v = stack.pop()
            if v in visited:
                return False
            visited.add(v)
            stack.extend(neighbor for neighbor in graph[v]
                          if neighbor not in visited)
        return True

def is_valid_output(graph):

    if not is_connected(graph):
        return False
    
    if not is_acyclic(graph):
        return False
    
    return True

def removeV(G, v):
    neigbors = G.pop(v)
    for n in neigbors:
        G[n].remove(v)
    return G

def solve(G, V, K):
    if is_connected(G):
        best = set(G.keys())
    else: 
        return 200
    
    if not K:
         return set()
    
    for v in V:
         if v not in K:
            newG = removeV(G, v)
            print(newG.keys())
            if is_valid_output(newG):
                new_best = solve(newG, V - {v}, K)
                if cost(new_best) < cost(best):
                    best = new_best
    
    return best

         

print(solve(G, V, K))