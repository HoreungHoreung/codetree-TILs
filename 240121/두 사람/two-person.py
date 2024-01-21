a1, g1 = input().split()
a2, g2 = input().split()

if (int(a1) >= 19) and (g1 == 'M') or (int(a2) >= 19) and (g2 == "M"):
    print(1)
else:
    print(0)