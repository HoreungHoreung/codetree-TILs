n, t = tuple(map(int, input().split()))
u_l = list(map(int, input().split()))
u_r = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    temp_1 = u_l[n-1]
    temp_2 = u_r[n-1]
    for i in range(n - 1, 0, -1):
        u_l[i] = u_l[i - 1]
    u_l[0] = d[n - 1]
    for i in range(n - 1, 0, -1):
        u_r[i] = u_r[i - 1]
    u_r[0] = temp_1
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp_2

for elem in u_l:
    print(elem, end = " ")
print()
for elem in u_r:
    print(elem, end = " ")
print()
for elem in d:
    print(elem, end = " ")