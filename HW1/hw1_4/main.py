test_cases = int(input())

for test_idx in range(test_cases):
    xyn = input().split()
    x = int(xyn[0])
    y = int(xyn[1])
    n = int(xyn[2])

    prices = set()
    for i in range(n+1):
        prices.add(i*x + (n-i)*y)

    prices = sorted(prices)

    print(' '.join(map(str, prices)))
