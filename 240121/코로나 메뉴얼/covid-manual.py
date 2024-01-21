A = 0
for _ in range(3):
    a, b = input().split()
    if (a == 'Y') and (int(b) >= 37):
        A += 1
if (A >= 2):
    print('E')
else:
    print('N')