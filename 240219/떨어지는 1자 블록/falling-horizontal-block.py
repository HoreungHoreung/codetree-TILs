n, m, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
k -= 1

def all_empty(row, col_s, col_e):
    for col in range(col_s, col_e + 1):
        if grid[row][col] == 1:
            return False
    return True

def get_target():
    for row in range(n - 1):
        if not all_empty(row + 1, k, k + m - 1):
            return row
    return n - 1

target_row = get_target()

for col in range(k, k + m ):
    grid[target_row][col] = 1

for row in range(n):
    for col in range(n):
        print(grid[row][col], end = " ")
    print()