n, t = tuple(map(int, input().split()))

conveyer_belt = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(t):
    temp = conveyer_belt[0][n - 1]
    for i in range(1, n):
        conveyer_belt[0][n - i] = conveyer_belt[0][n - i - 1] 
    conveyer_belt[0][0] = conveyer_belt[1][n - 1]
    
    for i in range(1, n):
        conveyer_belt[1][n - i] = conveyer_belt[1][n - i - 1]
    conveyer_belt[1][0] = temp

for i in range(n):
    print(conveyer_belt[0][i], end = " ")
print()
for i in range(n):
    print(conveyer_belt[1][i], end = " ")