import copy
class Graph:
    def __init__(self, G : dict = {}, terminals : set = set()) -> None:
        self.map = G
        self.visted = set()
        self.terminals = terminals
        self.N = len(self.map)

    def cost(self):
        return sum(len(neighbors) for neighbors in self.map.values()) // 2

    def is_connected(self):
        visited = set()
        stack = [0]
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                stack.extend(neighbor for neighbor in self.map[v] 
                            if neighbor not in visited)
        return len(visited) == len(self.map)
    
    def is_acyclic(self):
        visited = set()
        stack = set()

        def dfs(v):
            if v in stack:
                return False
            if v in visited:
                return True
            visited.add(v)
            stack.add(v)
            for neighbor in self.map[v]:
                if not dfs(neighbor):
                    return False
            stack.remove(v)
            return True

        for i in range(self.N):
            if not dfs(i):
                return False

G = { 0 : {1, 4, 2},
      1 : {0, 4}, 
      2 : {0, 4, 3},
      3 : {2},
      4 : {0, 1, 2} }
G2 
K = {0, 3}

graph = Graph(G, K)

print(graph.N)
print(graph.is_acyclic())

# def is_acyclic(graph):
#         visited = set()
#         stack = [i for i in range(len(graph))]
#         while stack:
#             v = stack.pop()
#             if v in visited:
#                 return False
#             visited.add(v)
#             stack.extend(neighbor for neighbor in graph[v]
#                           if neighbor not in visited)
#         return True

def is_valid_output(graph):

    if not is_connected(graph):
        return False
    
    if not is_acyclic(graph):
        return False
    
    return True

# def removeV(G, v):
#     neigbors = G.pop(v)
#     for n in neigbors:
#         G[n].remove(v)
#     return G

# def solve(G, V, K):
#     if is_connected(G):
#         best = set(G.keys())
#     else: 
#         return 200
    
#     if not K:
#          return set()
    
#     for v in V:
#          if v not in K:
#             newG = removeV(G, v)
#             print(newG.keys())
#             if is_valid_output(newG):
#                 new_best = solve(newG, V - {v}, K)
#                 if cost(new_best) < cost(best):
#                     best = new_best
    
#     return best

         

# print(solve(G, V, K))