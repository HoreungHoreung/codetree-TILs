n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
seq = [0 for _ in range(n)]

happy_nums = 0

def find_happy():
    consecutive, max_ccnt = 1, 1
    for i in range(1, n):
        if seq[i] == seq[i - 1]:
            consecutive += 1
        else:
            consecutive = 1
        max_ccnt = max(max_ccnt, consecutive)

    return max_ccnt >= m

for row in range(n):
    seq = grid[row][:]
 
    if find_happy():
        happy_nums += 1

for col in range(n):
    for row in range(n):
        seq[row] = grid[row][col]
    if find_happy():
        happy_nums += 1

print(happy_nums)