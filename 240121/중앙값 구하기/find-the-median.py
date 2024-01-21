a,b,c = tuple(map(int, input().split()))

if a > b and a < c:
    print(a)
elif a > b and a > c:
    if b < c:
        print(b)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)