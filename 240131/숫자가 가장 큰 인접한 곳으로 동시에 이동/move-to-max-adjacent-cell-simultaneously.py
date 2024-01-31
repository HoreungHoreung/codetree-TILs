n, m, t = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

next_count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def get_next_pos(curr_x, curr_y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    max_num, max_pos = 0, (0, 0)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy

        if in_range(next_x, next_y) and grid[next_x][next_y] > max_num:
            max_num = grid[next_x][next_y]
            max_pos = (next_x, next_y)
    
    return max_pos

def move(x, y):
    next_x, next_y = get_next_pos(x,y)
    next_count[next_x][next_y] += 1

def move_all():
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)

    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

def remove_dup():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0

def simulation():
    move_all()
    remove_dup()

    
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    count[x - 1][y - 1] = 1

for _ in range(t):
    simulation()

ans = 0
for i in range(n):
    for j in range(n):
        ans += count[i][j]

print(ans)