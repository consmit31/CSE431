N = int(input())

towers = []
for _ in range(N):
    inp = input().split()
    gain = int(inp[0])
    lost = int(inp[1])

    towers.append((gain, lost))

health = 0
start = 0
total_health = 0

for i in range(N):
    total_health += towers[i][0]-towers[i][1]

    if total_health < 0: 
        start = i + 1 
        health += total_health
        total_health = 0

print(start)

