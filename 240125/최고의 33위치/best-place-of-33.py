n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in  range(n)
]

def get_num_of_gold(row_s, row_e, col_s, col_e):
    num_of_gold = 0
    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            num_of_gold += arr[row][col]
    
    return num_of_gold


max_gold = 0

for row in range(n):
    for col in range(n):
        if row + 2 >= n:
            continue
        if col + 2 >= n:
            continue

        num_of_gold = get_num_of_gold(row, row + 2, col, col + 2)

        max_gold = max(max_gold, num_of_gold)

print(max_gold)