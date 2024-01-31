n = int(input())

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
max_gold = 0
def in_range(row, col):
    return row + 2 >= n or col + 2 >= n

def find_max_gold(row_s,row_e, col_s, col_e):
    curr_gold = 0
    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            curr_gold += grid[row][col]
    return curr_gold

for row in range(n):
    for col in range(n):
        if in_range(row, col):
            continue
        max_gold = max(max_gold, find_max_gold(row, row + 2, col, col + 2))

print(max_gold)