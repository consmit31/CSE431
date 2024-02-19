cases = int(input())

for _ in range(cases):
    inp = input().split()
    N, G = int(inp[0]), int(inp[1])

    diff = bin(N-G)
    if diff == 0:
        print(1)
        break
   
    print(diff.count('1'))

print(4 | 1)
    

    