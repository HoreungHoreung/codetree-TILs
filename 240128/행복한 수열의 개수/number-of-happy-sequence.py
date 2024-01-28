n, m = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def is_happy_row(row):
    consecutive = 1
    for i in range(n - 1):
        if grid[row][i] == grid[row][i + 1]:
            consecutive += 1
        else:
            consecutive = 1
        
        if consecutive >= m:
            return True

def is_happy_col(col):
    consecutive = 1
    for i in range(n - 1):
        if grid[i][col] == grid[i + 1][col]:
            consecutive += 1
        else:
            consecutive = 1

        if consecutive >= m:
            return True 

        


happy_sequence = 0
for row in range(n):
    if is_happy_row(row):
        happy_sequence += 1

for col in range(n):
    if is_happy_col(col):
        happy_sequence += 1



print(happy_sequence)