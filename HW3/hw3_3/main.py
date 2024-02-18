inp = input().split()
N = int(inp[0])
k = int(inp[1])

rooms = []
for _ in range(N):
    animals = int(input())
    rooms.append(animals)

print()
rooms.sort(reverse=True)
for i in range(k):
    print(rooms[i])