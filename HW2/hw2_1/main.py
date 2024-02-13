tests = int(input())

a = {}
c = 0
max = 0
for i in range(tests):
    x = int(input())
    if x in a:
        a[x] += 1
        if a[x] > c:
            c += 1
            max = x
    else:
        a[x] = 1

print(max)