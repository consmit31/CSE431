inp = input().split()

N = int(inp[0])
nidx = int(inp[1])

possible_colors = input().split()
visible_colors = input().split()

sum = 0
for color in visible_colors:
    sum += possible_colors.index(color)

guess_index = (nidx - sum) % N

guess = possible_colors[guess_index]

print(guess)

