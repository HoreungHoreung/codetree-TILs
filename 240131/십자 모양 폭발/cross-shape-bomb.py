n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp_array = [
    [0 for _ in range(n)]
    for _ in range(n)
]
r, c = list(map(int, input().split()))

center = grid[r-1][c-1]

def bomb(r,c,center):
    global grid
    for row in range(r - center, r + center - 1):
        for col in range(c - center, c + center -1):
            if row < 0 or row > n - 1 or col < 0 or col > n - 1:
                continue
            
            grid[row][c - 1] = 0 # 행 폭발
            grid[r - 1][col] = 0 # 열 폭발
def gravity():
    global grid
    for j in range(n):
        next_row = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                temp_array[next_row][j] = grid[i][j]
                next_row -= 1
    grid = temp_array




# def bomb(r,c,center):
#     global grid
#     for row in range(r - cente
# r + 1, r + center - 1):
#         if row < 0 or row > n - 1:
#             continue
#         grid[row][c - 1] = 0

bomb(r,c,center)
gravity()
for row in range(n):
    for col in range(n):
        print(grid[row][col], end = " ")
    print()