Am, Ae = tuple(map(int, input().split()))
Bm, Be = tuple(map(int, input().split()))

if (Am == Bm):
    if (Ae > Be):
        print('A')
    else:
        print('B')
elif (Am > Bm):
    print('A')
else:
    print('B')