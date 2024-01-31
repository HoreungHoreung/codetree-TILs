n, r, c = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

curr_x, curr_y = r - 1, c - 1
max_num = grid[curr_x][curr_y]

visited = []
visited.append(grid[curr_x][curr_y])


def in_range(x, y):
    return 0 <= x and x <= n and 0 <= y and y <= n

def can_move(x, y):
    return in_range(x, y) and grid[x][y] > grid[curr_x][curr_y]
    
def simulation():
    global curr_x, curr_y, max_num

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy

        if can_move(next_x, next_y):
            curr_x, curr_y = next_x, next_y
            visited.append(grid[curr_x][curr_y])
            return True
    return False

while True:
    if not simulation():
        break

for elem in visited:
    print(elem, end = " ")