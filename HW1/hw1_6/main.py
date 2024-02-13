import math
test_cases = int(input())

for test_idx in range(test_cases):
    xy = input().split()
    min = int(xy[0])
    max = int(xy[1])

    d = math.floor(max / 12) - math.ceil(min / 12) + 1

    s = 0
    b = 0
    for i in range(math.ceil(math.sqrt(min)), math.floor(math.sqrt(max))+1):
        s += 1
        if i**2 % 12 == 0:
            b += 1
    
    print(f"{d} {s} {b}")
    