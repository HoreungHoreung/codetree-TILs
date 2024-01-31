n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

temp = []

s1, e1 = tuple(map(int, input().split()))
s2, e2 = tuple(map(int, input().split()))

for i in range(n):
    if i < s1 - 1 or i > e1 - 1:
        temp.append(arr[i])
arr = temp

temp = []
for i in range(len(arr)):
    if i < s2 - 1 or i > e2 - 1:
        temp.append(arr[i])
arr = temp
print(len(arr))
for elem in arr:
    print(elem)