N = int(input())
nx, ny = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for _ in range(N):
    direction, distance = input().split()
    distance = int(distance)
    if (direction == 'E'):
        direction = 0
    elif (direction == 'S'):
        direction = 1
    elif (direction == 'W'):
        direction = 2
    else:
        direction = 3
    nx += dx[direction] * distance
    ny += dy[direction] * distance
print(nx, ny)