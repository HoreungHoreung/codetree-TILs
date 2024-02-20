n, m, t = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = [
    [0] * n
    for _ in range(n)
]

next_count = [
    [0] * n
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int,input().split()))
    count[r - 1][c - 1] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def move(x, y): #각 공을 다음 위치로 옮긴 next_count 배열을 최신화
    next_x, next_y = get_next_pos(x, y)
    next_count[next_x][next_y] += 1

def get_next_pos(curr_x, curr_y): #다음 공의 위치를 찾는함수
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_num = arr[curr_x][curr_y]
    max_pos = (curr_x, curr_y)
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        if in_range(next_x, next_y) and arr[next_x][next_y] > max_num:
            max_num = arr[next_x][next_y]
            max_pos = (next_x, next_y)
    return max_pos
    

def remove_duplicate_marbles():
    for i in range(n):
        for j in range(n):
            if next_count[i][j] > 1:
                next_count[i][j] = 0

def move_all(): #모든 공을 움직이는 함수
    #next_count, 즉 복사본의 배열을 초기화하는 단계 1
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    #count배열 안에서 각 공을 하나씩 움직이는 단계 2
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)
    
    remove_duplicate_marbles()
    
    for i in range(n):
        for j in range(n):
            count[i][j] = 0
    
    #next_count배열을 count배열로 옮기는 단계 4
    for i in range(n):
        for j in range(n):
            if next_count[i][j] == 1:
                count[i][j] = next_count[i][j]

cnt = 0

for _ in range(t):
    move_all()

for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            cnt += 1

print(cnt)