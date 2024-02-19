n, m, t = tuple(map(int, input().split()))
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

count = [
    [0] * n
    for _ in range(n)
]

new_count = [
    [0] * n
    for _ in range(n)
]

for _ in range(m):
    r,c = list(map(int, input().split()))
    count[r - 1][c - 1] = 1

def move(x, y):
    next_x, next_y = get_next_pos(x, y)
    new_count[next_x][next_y] += 1

def move_all():
    for i in range(n):
        for j in range(n):
            new_count[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)
    
    for i in range(n):
        for j in range(n):
            count[i][j] = new_count[i][j]

def get_next_pos(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_num, max_pos = arr[x][y], (x, y)
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if in_range(next_x, next_y) and arr[next_x][next_y] > max_num:
            max_num = arr[next_x][next_y]
            max_pos = (next_x, next_y)
    return max_pos


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate():
    move_all()
    remove_duplicate_marbles()

def remove_duplicate_marbles():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0

for _ in range(t):
    simulate()

cnt = 0
for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            cnt += 1
print(cnt)