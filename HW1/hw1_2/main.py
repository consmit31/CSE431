num_tests = int(input())

for test_idx in range(num_tests):
    line = input().split()
    S = int(line[0])
    k = int(line[1])

    for i in range(k):
        if S%2 == 1:
            S -= 15
            if S < 0:
                S += 1000000
            S = (S*2)%1000000
        else:
            S -= 99
            if S < 0:
                S += 1000000
            S = (S*3)%1000000

    print(S)