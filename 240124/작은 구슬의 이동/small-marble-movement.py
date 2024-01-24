n, t = tuple(map(int, input().split()))
r, c, d = input().split()
r,c = int(r), int(c)

dxs, dys = [0, -1, 1, 0], [1, 0, 0,-1]

mapper = {
    'R': 0,
    'U': 1,
    'D': 2,
    'L': 3,
    3 : 'L',
    2 : 'D',
    1 : 'U',
    0 : 'R'
}

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

for _ in range(t):
    if in_range(r + dxs[mapper[d]], c + dys[mapper[d]]):
        r += dxs[mapper[d]]
        c += dys[mapper[d]]
    else:
        d = mapper[3 - mapper[d]] 

print(r,c)