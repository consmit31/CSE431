tests = int(input())

for _ in range(tests):
    N_K = input().split()
    N = int(N_K[0])
    K = int(N_K[1])
    M = [int(x) for x in input().split()]

    sums = [float('-inf')] * (K + 1)
    sums[0] = 0

    for m in M:
        for i in range(m, K + 1):
            sums[i] = max(sums[i], sums[i - m] + m)

    result = max(sums)
    print(result)