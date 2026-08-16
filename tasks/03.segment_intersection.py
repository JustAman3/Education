a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
L = 0
R = 0
if a1 > a2:
    L = a1
else:
    L = a2
if b1 < b2:
    R = b1
else:
    r = b2
if L < R:
    print(L, R)
elif L == R:
    print(L)
else:
    print("пустое множество")
