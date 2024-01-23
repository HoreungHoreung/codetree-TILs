x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
direction = 3

command = input()
for elem in command:
    if elem == 'L':
        direction = (direction - 1) % 4
    elif elem == "R":
        direction = (direction + 1) % 4
    else:
        x += dx[direction]
        y += dy[direction]
print(x, y)