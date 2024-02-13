n, m, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def block_drop(m, k):
    global grid
    for i in range(1, n):
        for j in range(k - 1, m + k - 1):
            if grid[i][j] == 1:
                return i - 1
block_row = block_drop(m, k)

for i in range(k - 1, m + k - 1):
    grid[block_row][i] = 1

for row in range(n):
    for col in range(n):
        print(grid[row][col], end = " ")
    print()