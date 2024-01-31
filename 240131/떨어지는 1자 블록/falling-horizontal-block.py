n, m, k = tuple(map(int, input().split()))

block = [
    0 for _ in range(n)
]

for i in range(k - 1, k - 1 + m):
    block[i] = 1

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

lowest = 0


for row in range(n):
    cnt = 0
    for col in range(n):
        if not(grid[row][col] and block[col]):
            cnt += 1
    if cnt == n:
        lowest = row

for i in range(n):
    grid[lowest][i] += block[i]


for row in range(n):
    for col in range(n):
        print(grid[row][col], end = " ")
    print()