n, t = tuple(map(int, input().split()))

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

for i in range(n):
    arr_1.append(arr_2[i])

for _ in range(t):
    temp = arr_1[n*2 - 1]
    for i in range(n*2 - 1, 0, -1):
        arr_1[i] = arr_1[i-1]
    arr_1[0] = temp

for i in range(n):
    print(arr_1[i], end = ' ')
print()
for i in range(n,2*n):
    print(arr_1[i], end = ' ')