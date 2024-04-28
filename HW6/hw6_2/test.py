from main import convert_vertex_cover_to_k_clique

with open('test1.txt', 'r') as file:
    N, M, K = map(int, file.readline().split())
    edges = set()
    for _ in range(M):
        u, v = map(int, file.readline().split())
        if u > v:
            u, v = v, u  
        edges.add((u, v))

convert_vertex_cover_to_k_clique(N, K, edges)