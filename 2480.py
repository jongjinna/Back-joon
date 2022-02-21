a, b, c = map(int, input())
if a == b & b == c:
    print(a*1000 + 10000)
elif a == b:
    print(a*100 + 1000)
elif c == b:
    print(b*100 + 1000)
elif a == c:
    print(a*100 + 1000)
else:
    print(max(a, b, c) * 100)
