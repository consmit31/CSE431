inp = input().split()
m = int(inp[0]) # number of fights
n = int(inp[1]) # pieces of armor

C = list(int(x) for x in set(input().split()))

C.sort(reverse = True)
total_damage = 0
multiplier = 1

for i in range(m):
    total_damage += multiplier * C[i]
    if (i+1)%n == 0:
        multiplier += 1



print(total_damage)


