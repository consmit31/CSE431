bird_count = int(input())
distances = [int(distance) for distance in input().split()]
distances.sort()
i = 0
cur = distances[0]
while i < bird_count:
    print(bird_count-i)
    while i < bird_count and distances[i] == cur:
        i += 1
    if i < bird_count:
        cur = distances[i]

