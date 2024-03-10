inp = input().split()
m = int(inp[0]) # number of fights
n = int(inp[1]) # pieces of armor

C = list(int(x) for x in set(input().split()))

C.sort(reverse = True)
total_damage = 0
multiplier = 1

start_index = 0
if m == n:
    total_damage += sum(C)
while m > n:
    fights = C[start_index:start_index+n]
    total_damage += sum(fights) * multiplier

    m -= n
    start_index += n
    multiplier += 1

fights = C[start_index:]
if fights and m != n:
    total_damage += sum(fights) * multiplier

print(total_damage)


