n = int(input())
M = [int(x) for x in input().split()]

def GetMaxNonadjacent(n, M):
    if n == 1:
        return M[0]
    
    if n == 2:
        return max(M[0], M[1])
    
    max_sum = [0] * len(M)
    max_sum[0] = M[0]
    max_sum[1] = max(M[0], M[1])

    for i in range(2, n):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + M[i])

    return max_sum[-1]

print(GetMaxNonadjacent(n, M))