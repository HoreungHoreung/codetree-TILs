n, r, c = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

move_sequence = []

curr_x, curr_y = r - 1, c - 1
move_sequence.append(grid[curr_x][curr_y])

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate():
    global curr_x, curr_y, grid, move_sequence
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        if in_range(next_x, next_y) and  grid[next_x][next_y] > grid[curr_x][curr_y]:
            curr_x, curr_y = next_x, next_y
            move_sequence.append(grid[curr_x][curr_y])
            return True
    
    return False

while True:
    greater_number_exist = simulate()

    if not greater_number_exist:
        break

for num in move_sequence:
    print(num, end = " ")