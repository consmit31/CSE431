import copy
from graph import Graph

g1 = { 0 : {1, 4, 2},
      1 : {0, 4}, 
      2 : {0, 4, 3},
      3 : {2},
      4 : {0, 1, 2} }
K1 = {0, 3}
g3 = {0: {11, 6, 8},
      1: {3, 11, 10, 8},
      2: {14, 5, 12},
      3: {9, 4, 1},
      4: {3, 10},
      5: {6, 2},
      6: {0, 5, 14},
      7: {13, 14, 12},
      8: {1, 0, 13, 14},
      9: {11, 3},
     10: {4, 1, 13},
     11: {9, 0, 1},
     12: {7, 2},
     13: {10, 8, 7},
     14: {8, 6, 7, 2}}
K3 = {8, 9, 11, 14}


def solve(graph : Graph):
    if graph.numUnknown() == 0:
        if (graph.is_valid_output()):
            return graph.cost()
        else:
            return 200
        
    next = graph.getNextUnknown()
    
    next_graph1 = copy.deepcopy(graph)
    cost1 = solve(next_graph1)

    next_graph2 = copy.deepcopy(graph)
    next_graph2.removeV(next)
    cost2 = solve(next_graph2)  

    return min(cost1, cost2) 

def __main__():
    N, M, K = map(int, input().split())

    G = {i : set() for i in range(N)}
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].add(v)
        G[v].add(u)

    terminals = set()
    for i in range(K):
        terminals.add(int(input()))

    graph = Graph(G, terminals)

    print(G)

    # print(solve(graph))

__main__()