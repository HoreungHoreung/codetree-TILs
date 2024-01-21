m, f = tuple(map(int, input().split()))
if m >= 90:
    if f >= 95:
        print(10)
    elif f >= 90:
        print(5)
else:
    print(0)