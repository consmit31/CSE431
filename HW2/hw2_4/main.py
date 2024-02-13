from statistics import mean
import heapq

idx = int(input())

Ls = []
for i in range(idx):
    inp = input().split()
    Ls.append((int(inp[0]), int(inp[1])))

Ls.sort(key=lambda x: x[0])
current_time = 0
total_time = 0
pq = []
for a, d in Ls:
    while pq and pq[0] <= current_time:
        completed = heapq.heappop(pq)
        total_time += (current_time - completed)
    
    heapq.heappush(pq, current_time + d)
    current_time += d

while pq:
    completed = heapq.heappop(pq)
    total_time += (current_time - completed)

print(total_time//idx)