n, m = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def is_happy_row(row):
    consecutive = 1
    for i in range(1, n):
        if grid[row][i - 1] == grid[row][i]:
            consecutive += 1
        else:
            consecutive = 1
        
        if consecutive >= m:
            return True

def is_happy_col(col):
    consecutive = 1
    for i in range(1, n):
        if grid[i - 1][col] == grid[i][col]:
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

if n == 1 and m == 1:
    happy_sequence = 2

print(happy_sequence)