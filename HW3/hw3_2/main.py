def find_starting_tower(N, towers):
    current_health = 0
    starting_tower = 0
    total_health = 0

    for i in range(N):
        total_health += towers[i][0] - towers[i][1]

        # If the total health goes below 0, update the starting tower
        if total_health < 0:
            starting_tower = i + 1
            current_health += total_health
            total_health = 0

    return starting_tower

# Input reading
N = int(input())
towers = []
for _ in range(N):
    health_gain, health_lost = map(int, input().split())
    towers.append((health_gain, health_lost))

# Find the starting tower
result = find_starting_tower(N, towers)

# Output the result
print(result)
