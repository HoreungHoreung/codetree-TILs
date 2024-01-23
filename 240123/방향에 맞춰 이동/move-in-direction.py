N = int(input())
nx, ny = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for _ in range(N):
    direction, distance = input().split()
    distance = int(distance)
    if (direction == 'E'):
        nx, ny = nx + (distance * dx[0]), ny + (distance * dy[0])
    elif (direction == 'S'):
        nx, ny = nx + (distance * dx[1]), ny + (distance * dy[1])
    elif (direction == 'W'):
        nx, ny = nx + (distance * dx[2]), ny + (distance * dy[2])
    else:
        nx, ny = nx + (distance * dx[3]), ny + (distance * dy[3])
print(nx, ny)