MOD = 1000000009

T = int(input())

for _ in range(T):
    G, Ntotal = map(int, input().split())
    gate_types = list(map(int, input().split()))

    gates = [0] * (Ntotal + 1)
    gates[0] = 1

    for i in range(1, Ntotal + 1):
        for gate in gate_types:
            if i - gate >= 0:
                gates[i] = (gates[i] + gates[i - gate]) % MOD

    print(gates[Ntotal])

