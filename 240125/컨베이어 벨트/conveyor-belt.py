n, t = tuple(map(int, input().split()))
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

for _ in range(t):
    temp = arr_1[n-1]
    for i in range(n-1, 0, -1):
        arr_1[i] = arr_1[i-1]
    arr_1[0] = arr_2[n-1]
    for i in range(n-1, 0, -1):
        arr_2[i] = arr_2[i-1]
    arr_2[0] = temp

for elem in arr_1:
    print(elem, end = " ")
print()
for elem in arr_2:
    print(elem, end = " ")