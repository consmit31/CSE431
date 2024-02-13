test_cases = int(input())

for test_idx in range(test_cases):
    nmc = input().split()
    n = int(nmc[0])
    m = int(nmc[1])
    c = int(nmc[2])

    wings = fragments = n // m
    miles = wings
    while fragments >= c:
        wings = fragments // c
        miles += wings
        fragments = wings + (fragments % c)

    print(miles)


